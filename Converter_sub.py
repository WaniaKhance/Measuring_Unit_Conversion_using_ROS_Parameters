#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from math import pi
#fetching value from parameter named as converter
convert = rospy.get_param("converter")
#converting user published pound value to kilogram using fetched value from parameter
def convert_process(msg):
    #user published data from Convert topic
    a = msg.data
    kilogram = a * convert
    print(str(a) +" pound is converted to : "+ str(kilogram)+" kg")
# function definition
def convert_sub():
    #initializing subscriber node
    rospy.init_node("convert_sub_node")
    #subscribing to Convert topic of float msg type to send data to convert_process
    sub = rospy.Subscriber("Convert", Float32, convert_process)
#main function
if __name__ == '__main__':
    # Calling function
    convert_sub()
    #infinite loop till receives shutdown signal
    rospy.spin()
