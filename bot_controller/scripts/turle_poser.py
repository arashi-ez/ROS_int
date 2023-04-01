#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist 
from math import pi

rospy.init_node('draw_star')

turtle_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    # move forward
    move_cmd = Twist()
    move_cmd.linear.x = 1
    turtle_vel.publish(move_cmd)
    rospy.sleep(2)

    # rotate for 144 degrees (2.5 * pi)
    turn_cmd = Twist()
    turn_cmd.angular.z = 2.5 * pi / 180
    turtle_vel.publish(turn_cmd)
    rospy.sleep(1.25)

    # move forward again
    turtle_vel.publish(move_cmd)
    rospy.sleep(2)

    # rotate for another 144 degrees
    turtle_vel.publish(turn_cmd)
    rospy.sleep(1.25)

rospy.spin()
