#include <array>
#include <csignal>
#include <iostream>
#include <memory>

#include <ros/ros.h>

#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>
#include <cyphal/allocators/o1/o1_allocator.h>
#include <uavcan/node/Heartbeat_1_0.h>

#include <boost/stacktrace.hpp>

#include "connectors.h"

#include "utils.h"

std::shared_ptr<CyphalInterface> interface;

std::unique_ptr<BatteryService> battery_service;
std::unique_ptr<ButtonsService> buttons_service;
std::unique_ptr<HMIHandler> hmi_handler;
std::unique_ptr<PowerServicesProvider> power_services;

void error_handler() {std::cout << "Error in libcyhpal: " << std::endl << boost::stacktrace::stacktrace(); exit(1);}

uint32_t uptime = 0;
PREPARE_MESSAGE(uavcan_node_Heartbeat_1_0, hbeat)
void heartbeat() {
    uavcan_node_Heartbeat_1_0 heartbeat_msg = {.uptime = uptime, .health = {uavcan_node_Health_1_0_NOMINAL}, .mode = {uavcan_node_Mode_1_0_OPERATIONAL}};
    interface->SEND_MSG(uavcan_node_Heartbeat_1_0, &heartbeat_msg, hbeat_buf, uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_, &hbeat_transfer_id);
    uptime += 1;
}

static bool is_terminating = false;
void signalFinalizer(int signum) {
    if (is_terminating) {
        return;
    }
    is_terminating = true;

    std::cout << "Recieved termination signal" << std::endl;

    std::cout << "Attempting to delete battery_service" << std::endl;
    battery_service.reset();
    std::cout << "Attempting to delete buttons_service" << std::endl;
    buttons_service.reset();
    std::cout << "Attempting to delete power_services" << std::endl;
    power_services.reset();
    std::cout << "Attempting to delete hmi_handler" << std::endl;
    hmi_handler.reset();

    std::cout << "Checking if cyphal is running" << std::endl;
    if (interface->is_up()) {
        std::cout << "Processing last CAN TX messages. Deadline: +5s" << std::endl;
        uint64_t start = timeMillis();
        uint64_t now = start;
        while (interface->has_unsent_frames() && (now - start) < 5000) {
            interface->process_tx_once();
            now = timeMillis();
        }
    }

    ros::shutdown();

    exit(signum);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "listener");
    ros::NodeHandle ros_node;

    signal(SIGINT, signalFinalizer);
    signal(SIGTERM, signalFinalizer);

    interface = std::make_shared<CyphalInterface>(99);
    interface->setup<LinuxCAN, O1Allocator>("vcan2", 8*1024*10);  // 10 kb memory pool

    battery_service = std::make_unique<BatteryService>(interface, ros_node);
    buttons_service = std::make_unique<ButtonsService>(interface, ros_node);
    hmi_handler = std::make_unique<HMIHandler>(interface, ros_node);
    power_services = std::make_unique<PowerServicesProvider>(interface, ros_node);

    uint64_t last_heartbeat_time = 0;

    while (ros::ok()) {
        uint64_t tick = timeMillis();
        EACH_N_TICKS(1000, last_heartbeat_time, {
            heartbeat();
        })

        interface->loop();
        ros::spinOnce();
    }

    return 0;
}