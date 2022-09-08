#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from math import pi
# function definition for publishing user input data
def convert_pub():
    #initializing publisher node
    rospy.init_node("convert_pub_node")
    #creating topic named as Convert of float msg type
    pub = rospy.Publisher("Convert", Float32, queue_size = 10)
    rate = rospy.Rate(5)
    #an infinite loop till receives shutdown signal
    while not rospy.is_shutdown():
        convert = input("Please enter the amount in pound: ")
        #publishing user input on the 'Convert' topic with float type
        pub.publish(float(convert))
        rate.sleep()
#main function
if __name__ == '__main__':
    # calling function
    try:
        convert_pub()
    except rospy.ROSInterruptException:
        pass
