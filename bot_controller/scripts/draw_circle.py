#!/usr/bin/env python3 
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("I am going to Draw a Circle")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/turtle1/cmd_vel")
