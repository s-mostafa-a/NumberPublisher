#include <ros/ros.h>
#include <stdio.h>
#include <iostream>
#include <std_msgs/String.h>
#include <sstream>
//ros::NodeHandle n;
ros::Publisher say_pub;


void publishKon(std::string s){
  std_msgs::String payam;
  payam.data = s;
  say_pub.publish(payam);
}

int main(int argc, char** argv)
{ 
  ros::init(argc, argv, "image_converter");
  ros::NodeHandle nh_;
  say_pub = nh_.advertise<std_msgs::String>("/sayings", 1000);
  //ImageConverter ic;
  int i = 0;
  while (ros::ok()) {
  i++;
  std::ostringstream convert ;
  convert << i;
  std::string s = "number ";
  s = s + convert.str();
  ROS_INFO("Number %d", i);
  publishKon(s);
  ros::Duration(2).sleep();
  }
  ros::spin();
  return 0;
}

