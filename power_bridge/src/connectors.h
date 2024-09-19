#pragma once

#include <string>

#include <ros/ros.h>

#include <cyphal/subscriptions/subscription.h>

#include <mors/HMIBeeper.h>
#include <mors/HMILed.h>
#include <mors/PowerReset.h>
#include <voltbro/battery/state_1_0.h>
#include <voltbro/battery/buttons_1_0.h>
#include <sensor_msgs/BatteryState.h>

class BatteryService : public AbstractSubscription<voltbro_battery_state_1_0> {
private:
    DESERIALIZE_TYPE(voltbro_battery_state_1_0, interface)

    ros::Publisher bat_publisher;
public:
    BatteryService(const std::shared_ptr<CyphalInterface> interface, ros::NodeHandle&);
    void handler(
        const voltbro_battery_state_1_0& bat_info,
        CanardRxTransfer* transfer
    ) override;
};

class ButtonsService : public AbstractSubscription<voltbro_battery_buttons_1_0> {
private:
    DESERIALIZE_TYPE(voltbro_battery_buttons_1_0, interface)

    ros::Publisher buttons_publisher;
public:
    ButtonsService(const std::shared_ptr<CyphalInterface> interface, ros::NodeHandle&);
    void handler(
        const voltbro_battery_buttons_1_0& bat_info,
        CanardRxTransfer* transfer
    ) override;
};

template <typename T>
class ROSHandler {
private:
    ros::Subscriber subscriber;
public:
    ROSHandler(ros::NodeHandle& node, const std::string& topic, size_t queue_size) {
        subscriber = node.subscribe(topic, queue_size, &ROSHandler::callback, this);
        std::cout << "Subscribed to topic <" << topic << ">" << std::endl;
    }
    ROSHandler(ros::NodeHandle& node, const std::string& topic)
        : ROSHandler(node, topic, 10) {}
    virtual void callback(typename T::ConstPtr) = 0;
};


template <typename T>
class ROSServiceProvider {
private:
    ros::ServiceServer service;
public:
    virtual bool callback(typename T::Request&, typename T::Response&) = 0;

    ROSServiceProvider(ros::NodeHandle& node, const std::string& service_name) {
        service = node.advertiseService(service_name, &ROSServiceProvider::callback, this);
        std::cout << "Providing service <" << service_name << ">" << std::endl;
    }
};


class HMIHandler : public ROSHandler<mors::HMIBeeper>, public ROSHandler<mors::HMILed> {
public:
    enum class Interface: uint8_t {LED_1 = 0, LED_2 = 1};
private:
    const std::shared_ptr<CyphalInterface> interface;

    std::map<Interface, std::array<uint8_t, 3>> last_colors;
public:

    HMIHandler(
        const std::shared_ptr<CyphalInterface> interface,
        ros::NodeHandle& node
    ) : ROSHandler<mors::HMIBeeper>(node, "/hmi/beeper"),
        ROSHandler<mors::HMILed>(node, "/hmi/led"),
        interface(interface) {}
    void send_beep(float duration, float frequency);
    void send_color(uint8_t r, uint8_t g, uint8_t b);
    void reset_color();

    void send_color(
        Interface hmi_interface,
        uint8_t r,
        uint8_t g,
        uint8_t b,
        float duration = 0,
        float frequency = 0
    );
    void set_last_color(Interface hmi_interface, uint8_t r, uint8_t g, uint8_t b);
    void reset_color(Interface hmi_interface);

    void callback(mors::HMIBeeper::ConstPtr msg) override;
    void callback(mors::HMILed::ConstPtr msg) override;
    ~HMIHandler();
};

class PowerServicesProvider: ROSServiceProvider<mors::PowerReset> {
private:
    const std::shared_ptr<CyphalInterface> interface;
public:
    PowerServicesProvider(const std::shared_ptr<CyphalInterface> interface, ros::NodeHandle& node):
        ROSServiceProvider(node, "/power/reset"),
        interface(interface) {}
    bool callback(mors::PowerReset::Request&, mors::PowerReset::Response&) override;
    void call_reboot();
};
