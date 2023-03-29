#/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_nide")
    rospy.logwarn("This is a warning")
    rospy.logerr("Error")

    rospy.sleep(1.0)

    rospy.loginfo("GGs")
