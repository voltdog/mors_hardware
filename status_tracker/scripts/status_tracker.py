#!/usr/bin/env python
import rospy
import time
import os
from mors.msg import HMIBeeper, HMILed, PowerButtons
from std_msgs.msg import Bool
from mors.srv import JointsCmd

class StatusTracker():
    def __init__(self) -> None:
        rospy.init_node("status_tracker")

        rospy.Subscriber("power/buttons", PowerButtons, self.btn_callback)

        self.led_pub = rospy.Publisher('/hmi/led', HMILed, queue_size=1)
        self.beep_pub = rospy.Publisher('hmi/beeper', HMIBeeper, queue_size=10)
        self.disable_pub = rospy.Publisher('disable', Bool, queue_size=10)

        self.rate = rospy.Rate(10)

        self.led_msg = HMILed()
        self.beep_msg = HMIBeeper()
        self.disable_msg = Bool()

        self.emerg_btn = False
        self.pre_emerg_btn = False
        self.user_btn = False
        self.pre_user_btn = False
        self.emerg_on = False
        self.emerg_off = False

        self.user_btn_on = False

    def run(self):
        rospy.sleep(0.5)
        self.set_led(1, 10, 0, 0, 1, 0)
        rospy.loginfo("status_tracker started")
        while not rospy.is_shutdown():
            self.check_emerg()
            
            if self.emerg_on == True:
                self.disable_msg.data = True
                self.set_led(1, 10, 0, 0, 2000, 8)
                self.set_beep(2, 8)

            if self.emerg_off == True:
                os.system("cd ~")
                os.system("./start_offsets.sh")
                self.disable_msg.data = False
                self.set_led(1, 10, 0, 0, 0, 0)
                print("idle")
                self.set_beep(0, 8)

            if self.user_btn == True and self.pre_user_btn == False:
                self.user_btn_on = not self.user_btn_on
                if self.user_btn_on == True:
                    rospy.loginfo("User Button On")
                    self.set_joint_kp([0.0]*12)
                    self.set_joint_kd([0.7]*12)
                    self.disable_msg.data = True
                    self.set_led(1, 10, 0, 0, 2000, 8)
                    self.set_beep(0.5, 4)
                else:
                    rospy.loginfo("User Button Off")
                    self.set_joint_kp([0.0]*12)
                    self.set_joint_kd([0.0]*12)
                    self.disable_msg.data = False
                    self.set_led(1, 10, 0, 0, 0, 0)


            self.disable_pub.publish(self.disable_msg)
            self.pre_emerg_btn = self.emerg_btn
            self.pre_user_btn = self.user_btn
            self.rate.sleep()

    def set_mode(self, mode):
        rospy.wait_for_service('joints_kp')
        try:
            set_kp_srv = rospy.ServiceProxy('joints_kp', JointsCmd)
            resp = set_kp_srv(kp)
            return resp.result
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def set_joint_kp(self, kp):
        rospy.wait_for_service('joints_kp')
        try:
            set_kp_srv = rospy.ServiceProxy('joints_kp', JointsCmd)
            resp = set_kp_srv(kp)
            return resp.result
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def set_joint_kd(self, kd):
        rospy.wait_for_service('joints_kd')
        try:
            set_kd_srv = rospy.ServiceProxy('joints_kd', JointsCmd)
            resp = set_kd_srv(kd)
            return resp.result
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


    def check_emerg(self):
        if self.emerg_btn == True and self.pre_emerg_btn == False:
            print("emerg on")
            self.emerg_on = True
        else:
            self.emerg_on = False

        if self.emerg_btn == False and self.pre_emerg_btn == True:
            print("emerg off")
            self.emerg_off = True
        else:
            self.emerg_off = False

    def set_led(self, interface, r=10, g=0, b=0, dur=0, freq=0):
        self.led_msg.r = r
        self.led_msg.g = g
        self.led_msg.b = b
        self.led_msg.duration = dur
        self.led_msg.frequency = freq
        self.led_msg.interface = interface
        self.led_pub.publish(self.led_msg)

    def set_beep(self, duration, frequency):
        self.beep_msg.duration = duration
        self.beep_msg.frequency = frequency
        self.beep_pub.publish(self.beep_msg)

    def btn_callback(self, data : PowerButtons):
        if data.emergency == True:
            # rospy.loginfo("Emergency Button")
            self.emerg_btn = True
        else:
            self.emerg_btn = False
        if data.user == True:
            # rospy.loginfo("User Button")
            self.user_btn = True
        else:
            self.user_btn = False



def main():
    tracker = StatusTracker()
    tracker.run()

if __name__ == '__main__':
    main()
