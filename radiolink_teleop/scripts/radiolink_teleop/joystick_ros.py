import rospy
import time
import hid
from sensor_msgs.msg import Joy

RX = 0
RY = 1
LX = 2
LY = 3
R1 = 5
R2 = 4
L2 = 6
L1 = 7

VENDOR_ID = 0x0483
DEVICE_ID = 0x5710
 
CONNECTED = 1
RECEIVER_ERROR = 2
JOYSTICK_ERROR = 3
ACCESS_ERROR = 4

class Joystick:
    def __init__(self) -> None:
        self.joy_value = [0]*8
        self.__status = 0
        self.__pause = False
        self.data = [0]*8

        self.err_lst1 = (0)*8
        self.err_lst2 = (0, 0, 1, 0, 0, 0, 0, 0)
        
        rospy.Subscriber("joy", Joy, self.joy_callback, queue_size=1)     
        
    def joy_callback(self, msg : Joy):
        # print(msg.axes)
        self.data = msg.axes
        self.joy_value[RX] = -self.data[0]
        self.joy_value[RY] = -self.data[1]
        self.joy_value[LY] = -self.data[2]
        self.joy_value[LX] = -self.data[3]

        self.joy_value[R2] = self.data[4]
        self.joy_value[R1] = self.data[5]
        self.joy_value[L2] = self.data[6]
        self.joy_value[L1] = self.data[7]
      
        if self.data == self.err_lst1 or self.data == self.err_lst2:
            self.__status = JOYSTICK_ERROR
        else:
            self.__status = CONNECTED

    # def read_data(self):
    #     # if self.__status != RECEIVER_ERROR:
    #     #     try:
    #     #         data = self.device.read(16, 100)
    #     #     except:
    #     #         self.__status = JOYSTICK_ERROR
    #     #         return -1
    #         # print((data[10] | (data[11] << 8))-557)

    #     # if len(self.data) == 8:
    #     self.joy_value[RX] = self.data[0]
    #     self.joy_value[RY] = self.data[1]
    #     self.joy_value[LY] = self.data[2]
    #     self.joy_value[LX] = self.data[3]

    #     self.joy_value[R2] = self.data[4]
    #     self.joy_value[R1] = self.data[5]
    #     self.joy_value[L2] = self.data[6]
    #     self.joy_value[L1] = self.data[7]

    #     print(self.joy_value[RX])
    #     return 1
    #     # else:
    #     #     self.__status = JOYSTICK_ERROR
    #     #     return -1

    
    # def loop_read(self):
    #     while True:
    #         self.read_data()

    # def pause_loop(self):
    #     self.__pause = True

    # def play_loop(self):
    #     self.__pause = False

    def get_joy_data(self):
        return self.joy_value


    def get_joy_status(self):
        return self.__status
    


if __name__ == "__main__":
    joy = Joystick()

    while(1):
        status = joy.get_joy_status()

        if status == CONNECTED:
            if joy.read_data() == 1:
                lst = joy.get_joy_data()
                for i in lst:
                    print(i)
                print("===========")
        elif status == RECEIVER_ERROR:
            print("Receiver disconnected. Trying to connect...")
            joy.connect()
            time.sleep(2)
        elif status == JOYSTICK_ERROR:
            print("Joystick disconnected. Please turn it on or connect the receiver...")
            joy.connect()
            joy.read_data()
            time.sleep(2)
        elif status == ACCESS_ERROR:
            print("ERROR: You don't have permission to open this USB-device!")
            break

        time.sleep(0.01)


    




