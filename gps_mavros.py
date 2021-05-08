#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from sensor_msgs.msg import NavSatFix



def gps_durum(data):
    rospy.loginfo("Current Latitude degrees : %2f ", data.latitude)
    rospy.loginfo("Current Longitude degrees : %2f ", data.longitude)
    rospy.loginfo("Current Altitude : %2f ", data.altitude)
    print("##########################################################")

def do_cur_gps():
    rospy.init_node("mavcmd", anonymous=True)
    rospy.Subscriber("/mavros/global_position/global",NavSatFix,gps_durum)
    rospy.spin()


do_cur_gps()    
