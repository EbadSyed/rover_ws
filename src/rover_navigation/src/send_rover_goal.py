#!/usr/bin/env python
from __future__ import print_function
import rospy
import actionlib
import actionlib_tutorials.msg
import tf
from geometry_msgs.msg import PoseStamped 
rate = rospy.Rate(10.0) #set spin rate to 10 Hz
pub = rospy.Publisher('move_base', PoseStamped , queue_size=1)
def fibonacci_client():
	client = actionlib.SimpleActionClient('move_base', actionlib_tutorials.msg.PoseStamped)
	result = fibonacci_client()
	client.wait_for_server()
	goal = actionlib_tutorials.msg.PoseStamped()
	goal.posithion.x=1
	goal.posithion.y=1
	goal.posithion.z=0
	goal.orentation.x=1
	goal.orentation.y=1
	goal.orentation.z=1
	goal.orentation.w=0
	client.send_goal(goal)
	client.wait_for_result()
	return client.get_result()


if __name__ == '__main__':
	try:
		rospy.init_node('send_rover_goal.py')
		result = fibonacci_client()
		print str(result)
	except:
		print "noo"
		pass







