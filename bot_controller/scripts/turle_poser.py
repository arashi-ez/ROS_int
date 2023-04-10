#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 

def pose_callback(pose : Pose):
    cmd = Twist()
    #if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
    #    cmd.linear.x = 0.0
    #    cmd.angular.z = math.pi/math.radians(180) 

    #U need to make a def which will move turtle after turning 180 degrees
    if pose.x == 5.5: 
        cmd.linear.x = 0.0
        cmd.angular.z = math.pi/math.radians(180)
    elif a: 
        pass
    else:
        cmd.linear.x = 2.0
        cmd.angular.z = 0.0
    pub.publish(cmd)
    

if __name__=='__main__':
    rospy.init_node("turtle_poser")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback) 
    rospy.loginfo("NODE IS STARTING")

    rospy.spin()