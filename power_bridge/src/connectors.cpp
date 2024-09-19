#include "connectors.h"

#include <uavcan/node/ExecuteCommand_1_1.h>
#include <voltbro/hmi/beeper_service_1_0.h>
#include <voltbro/hmi/led_service_1_0.h>
#include <mors/PowerButtons.h>

#define CID_PWR 9


static uint8_t beeper_buf[voltbro_hmi_beeper_service_Request_1_0_EXTENT_BYTES_];
static CanardTransferID beeper_transfer_id = 0;
#define SRV_HMI_BEEPER_PORT 258
void HMIHandler::send_beep(float duration, float frequency) {
    voltbro_hmi_beeper_service_Request_1_0 beeper_msg = {0};
    beeper_msg.frequency.hertz = frequency;
    beeper_msg.duration.second = duration;

    interface->SEND_TRANSFER(
        voltbro_hmi_beeper_service_Request_1_0,
        &beeper_msg,
        beeper_buf,
        SRV_HMI_BEEPER_PORT,
        &beeper_transfer_id,
        CanardPriorityNominal,
        CanardTransferKindRequest,
        CID_PWR
    );
}

void HMIHandler::callback(mors::HMIBeeper::ConstPtr msg) {
    ROS_INFO("Beep! dur=%f freq=%f", msg->duration, msg->frequency);
    send_beep(msg->duration, msg->frequency);
}

static uint8_t led_buf[voltbro_hmi_led_service_Request_1_0_EXTENT_BYTES_];
static CanardTransferID led_transfer_id = 0;
#define SRV_HMI_LED_PORT 172
void HMIHandler::send_color(
    Interface hmi_interface,
    uint8_t r,
    uint8_t g,
    uint8_t b,
    float duration,
    float frequency
) {
    ROS_INFO(
        "Sending color (%d %d %d) to interface %d with d=%f, f=%f",
        r, g, b, hmi_interface, duration, frequency
    );

    voltbro_hmi_led_service_Request_1_0 led_msg = {0};
    led_msg.r.value = r;
    led_msg.g.value = g;
    led_msg.b.value = b;

    led_msg.duration.second = duration;
    led_msg.frequency.hertz = frequency;

    led_msg.interface.value = static_cast<int8_t>(hmi_interface);

    interface->SEND_TRANSFER(
        voltbro_hmi_led_service_Request_1_0,
        &led_msg,
        led_buf,
        SRV_HMI_LED_PORT,
        &led_transfer_id,
        CanardPriorityNominal,
        CanardTransferKindRequest,
        CID_PWR
    );
}

void HMIHandler::send_color(
    uint8_t r,
    uint8_t g,
    uint8_t b
) {
    send_color(Interface::LED_1, r, g, b, 0, 0);
}

void HMIHandler::set_last_color(
    Interface hmi_interface,
    uint8_t r,
    uint8_t g,
    uint8_t b
) {
    last_colors[hmi_interface] = {r, g, b};
}

void HMIHandler::reset_color() {
    for (auto const& [hmi_interface, color] : last_colors) {
        send_color(hmi_interface, color[0], color[1], color[2]);
    }
}

void HMIHandler::reset_color(Interface hmi_interface) {
    std::array<uint8_t, 3>& color = last_colors[hmi_interface];
    send_color(hmi_interface, color[0], color[1], color[2]);
}

void HMIHandler::callback(mors::HMILed::ConstPtr msg) {
    Interface hmi_interface = static_cast<Interface>(msg->interface);

    set_last_color(hmi_interface, msg->r, msg->g, msg->b);
    send_color(hmi_interface, msg->r, msg->g, msg->b, msg->duration, msg->frequency);
}

HMIHandler::~HMIHandler() {
    send_color(Interface::LED_1, 10, 0, 0);
    send_color(Interface::LED_2, 0, 0, 0);
    send_beep(0.5, 4);
}

static uint8_t command_buf[uavcan_node_ExecuteCommand_Request_1_1_EXTENT_BYTES_];
static CanardTransferID command_transfer_id = 0;
void PowerServicesProvider::call_reboot() {
    uavcan_node_ExecuteCommand_Request_1_1 command = {0};
    command.command = uavcan_node_ExecuteCommand_Request_1_1_COMMAND_RESTART;

    interface->SEND_TRANSFER(
        uavcan_node_ExecuteCommand_Request_1_1,
        &command,
        command_buf,
        uavcan_node_ExecuteCommand_1_1_FIXED_PORT_ID_,
        &command_transfer_id,
        CanardPriorityNominal,
        CanardTransferKindRequest,
        CID_PWR
    );
}

bool PowerServicesProvider::callback(
    mors::PowerReset::Request& request,
    mors::PowerReset::Response& response
) {
    // TODO: real response
    call_reboot();
    response.ok = true;
    return true;
}


BatteryService::BatteryService(const std::shared_ptr<CyphalInterface> interface, ros::NodeHandle& node) :
    AbstractSubscription(
        interface,
        CanardTransferKindMessage,
        7993,
        voltbro_battery_state_1_0_EXTENT_BYTES_
    ) {
    const std::string bat_str = "bat";
    bat_publisher = node.advertise<sensor_msgs::BatteryState>(bat_str, 5);
    std::cout << "Publishing topic <" << bat_str << ">" << std::endl;
}

void BatteryService::handler(
    const voltbro_battery_state_1_0& bat_info,
    CanardRxTransfer* transfer
) {
    sensor_msgs::BatteryState battery;
    battery.voltage = bat_info.voltage.volt;
    battery.current = bat_info.current.ampere;
    battery.charge = bat_info.charge.coulomb / 3.6;
    battery.capacity = bat_info.capacity.coulomb / 3.6;
    battery.percentage = battery.charge / battery.capacity;

    battery.design_capacity = bat_info.design_capacity.coulomb / 3.6;

    battery.power_supply_status = bat_info.power_supply_status.value;
    battery.power_supply_health = bat_info.power_supply_health.value;
    battery.power_supply_technology = bat_info.power_supply_technology.value;
    battery.present = bat_info.is_present.value == 1 ? true : false;

    battery.location = std::string(
        (char*)bat_info.location.value.elements,
        bat_info.location.value.count
    );
    battery.serial_number = std::string(
        (char*)bat_info.serial_number.value.elements,
        bat_info.serial_number.value.count
    );

    bat_publisher.publish(battery);
}

ButtonsService::ButtonsService(const std::shared_ptr<CyphalInterface> interface, ros::NodeHandle& node) :
    AbstractSubscription(
        interface,
        CanardTransferKindMessage,
        8003,
        voltbro_battery_buttons_1_0_EXTENT_BYTES_
    ) {
    const std::string butttons_str = "power/buttons";
    buttons_publisher = node.advertise<mors::PowerButtons>(butttons_str, 5);
    std::cout << "Publishing topic topic <" << butttons_str << ">" << std::endl;
}

void ButtonsService::handler(
    const voltbro_battery_buttons_1_0& buttons_info,
    CanardRxTransfer* transfer
) {
    mors::PowerButtons buttons;

    buttons.emergency = buttons_info.emergency_button.value;
    buttons.user = buttons_info.user_button.value;

    buttons_publisher.publish(buttons);
}
