#! /usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("galacts_first_time_test")
    rospy.loginfo("Test node has been started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Ez Pz")
        rate.sleep()
    if rospy.is_shutdown():{
        rospy.logwarn("omg!!!")    
    }
