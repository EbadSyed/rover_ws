#!/usr/bin/env python
################### import ###########################
import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
############# creation of objects
distance=Twist()
#####################
############# node initialization ####################
rospy.init_node('joystick', anonymous=True) #init_node
############# creation variables #######################
flag = True
#flag is set when obstacle detected
############ definitions of functions ##################
def clbk_obstacle(data):
	global flag
	check = data.range
	if check <= 0.5:
		flag = True
	else:
		flag = False
#get value of distance
#obstacle at 0.5m
def clbk_drive(data):
	global distance
	#msg object to publish data
	rospy.loginfo(data)
	#if data.axes[1]!=0 or data.axes[2]!=0:
	distance.linear.x=data.axes[1]
	distance.angular.z=data.axes[0]*(2)
	pub.publish(distance)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) #publisher velocity
#### definition of publisher/subscriber and services ###
rospy.Subscriber("joy", Joy, clbk_drive)
#subscriber joystick
rospy.Subscriber("range", Range, clbk_obstacle)
#subscriber ir-ranger

############# main program #############################
rate = rospy.Rate(10)
#--------------endless loop till shut down -------------#
while not rospy.is_shutdown():
	#if flag == True:
	#	distance.linear.x = 0
	
	rate.sleep()
