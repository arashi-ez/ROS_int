#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose 
from geometry_msgs.msg import Twist 
from turtlesim.srv import SetPen

def call_set_pen_sevice(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose : Pose):
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.2
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    pub.publish(cmd)

if __name__=='__main__':
    rospy.init_node("turtle_poser")
    rospy.wait_for_service("/turtle1/set_pen")
    call_set_pen_sevice(255, 0, 0, 3, 0)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback) 
    rospy.loginfo("NODE IS STARTING")

    rospy.spin()