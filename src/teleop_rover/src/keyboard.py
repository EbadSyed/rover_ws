#!/usr/bin/env python
################### import ###########################
import rospy
from std_msgs.msg import String
#keyboard cmd message type
from geometry_msgs.msg import Twist
#turtle cmd_vel message type
############# creation of objects
#####################
############# node initialization ####################
rospy.init_node('keyboard_control', anonymous=True)
##### initialize values ####
cmd_vel_topic = rospy.get_param('cmd_vel_topic', '/turtle1/cmd_vel')
key_cmd_topic = rospy.get_param('key_cmd_topic', '/keyboard_cmd')
speed_scaling = rospy.get_param('speed_scaling', 1)
############ definitions of functions ##################
def callback(msg):
    global speed_scaling
    move = Twist()
    if msg.data == "UP":
        move.linear.x = 1
    elif msg.data == "DOWN":
        move.linear.x = -1
    elif msg.data == "LEFT":
        move.angular.z = 1
    elif msg.data == "RIGHT":
        move.angular.z = -1

    elif msg.data == "PLUS":
        speed_scaling += 1
    elif msg.data == "MINUS":
        speed_scaling -= 1

    move.linear.x = move.linear.x * speed_scaling
    move.angular.z = move.angular.z * speed_scaling
    
    pub.publish(move)
#### definition of publisher/subscriber and services ###
rospy.Subscriber(key_cmd_topic, String, callback)
pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=1)
############# main program #############################
#--------------endless loop till shut down -------------#
rospy.spin()