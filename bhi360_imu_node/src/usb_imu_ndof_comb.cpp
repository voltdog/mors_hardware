#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/Imu.h"

#include <sstream>

#include <stdio.h> // printf
#include <wchar.h> // wchar_t

#include "hidapi/hidapi.h"

int open_imu_hid(void);

#define MAX_STR 255

hid_device *acc_handle;

int open_imu_hid()
{
	int res;
	unsigned char buf[65];
	wchar_t wstr[MAX_STR];

	int i;

	// Initialize the hidapi library
	res = hid_init();
	
	struct hid_device_info *imu_info;
	imu_info = hid_enumerate(0xCafe, 0x4004);

	ROS_INFO("First interface path is %s", imu_info->path);

	acc_handle = hid_open_path(imu_info->path);
	if (!acc_handle) {
		ROS_INFO("Unable to open IMU!");
		hid_exit();
 		return 1;
	}
	
	//hid_set_nonblocking(acc_handle, 1);

	ROS_INFO("IMU interface is opened successfully!");

	// Read the Manufacturer String
	res = hid_get_manufacturer_string(acc_handle, wstr, MAX_STR);
	ROS_INFO("Manufacturer String: %ls", wstr);

	// Read the Product String
	res = hid_get_product_string(acc_handle, wstr, MAX_STR);
	ROS_INFO("Product String: %ls", wstr);

	// Read the Serial Number String
	res = hid_get_serial_number_string(acc_handle, wstr, MAX_STR);
	ROS_INFO("Serial Number String: (%d) %ls", wstr[0], wstr);
	
	return 0;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");

  ros::NodeHandle n;

  ros::Publisher imu_pub = n.advertise<sensor_msgs::Imu>("imu", 1000);

  ros::Rate loop_rate(100);
  
  uint8_t device_present = 1;
  
  if( open_imu_hid() )
  { 
  	return 1;
  }

  int count = 0;
  while (ros::ok())
  {
  	sensor_msgs::Imu imu_msg;
  	
  	uint8_t buffer[64];
	int8_t bytes_number = 0;
	
	while( device_present )
	{
		bytes_number = hid_read(acc_handle, buffer, 64);
		
		if( bytes_number < 0 )
		{
			device_present = 0;
		}
		else if( bytes_number )
		{
			int16_t acc_x = *(int16_t*)&buffer[2];
			int16_t acc_y = *(int16_t*)&buffer[4];
			int16_t acc_z = *(int16_t*)&buffer[6];
			
			imu_msg.linear_acceleration.x = acc_x * 9.81f * 1.0f / 4096.0f;
			imu_msg.linear_acceleration.y = acc_y * 9.81f * 1.0f / 4096.0f;
			imu_msg.linear_acceleration.z = acc_z * 9.81f * 1.0f / 4096.0f;
			
			int16_t gyr_x = *(int16_t*)&buffer[8];
			int16_t gyr_y = *(int16_t*)&buffer[10];
			int16_t gyr_z = *(int16_t*)&buffer[12];
			
			imu_msg.angular_velocity.x = gyr_x * 6.28f * 2000.0f / 32768.0f / 360.0f;
			imu_msg.angular_velocity.y = gyr_y * 6.28f * 2000.0f / 32768.0f / 360.0f;
			imu_msg.angular_velocity.z = gyr_z * 6.28f * 2000.0f / 32768.0f / 360.0f;	
			
			int16_t quat_x = *(int16_t*)&buffer[14];
			int16_t quat_y = *(int16_t*)&buffer[16];
			int16_t quat_z = *(int16_t*)&buffer[18];
			int16_t quat_w = *(int16_t*)&buffer[20];
			
			imu_msg.orientation.x = quat_x * 1.0f / 16384.0f;
			imu_msg.orientation.y = quat_y * 1.0f / 16384.0f;
			imu_msg.orientation.z = quat_z * 1.0f / 16384.0f;
			imu_msg.orientation.w = quat_w * 1.0f / 16384.0f;
			
			imu_msg.header.stamp.nsec = *(uint32_t*)&buffer[24] * 1000;
			
			break ;	
							
		}
		else
		{
			break ;
		}
	}
	
	if( !device_present )
	{
		ROS_INFO("%s", "USB error!");
		return 0;
	}

    //ROS_INFO("%s", msg.data.c_str());

    imu_pub.publish(imu_msg);

    ros::spinOnce();

    //loop_rate.sleep();
    ++count;
  }


  return 0;
}

