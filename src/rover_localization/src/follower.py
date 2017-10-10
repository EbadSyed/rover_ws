#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import Twist
rospy.init_node('node_listener') #init node
listener = tf.TransformListener() #setup tf listener
rate = rospy.Rate(10.0) #set spin rate to 10 Hz
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
#lookup for the newest transform
	try:
		(trans,rot)=listener.lookupTransform('/camera_link', '/ar_marker_3',
		rospy.Time(0))
		#get euler angles form quaternions
		euler =tf.transformations.euler_from_quaternion(rot)
		#print translation and rotation
		print 'translation: ',trans
		print 'rotation: ',euler
		print '########'
		distance=Twist()
		distance.linear.x=trans[2]-1
		distance.angular.z=trans[0]*6
		pub.publish(distance)

	except (tf.LookupException, tf.ConnectivityException,
	tf.ExtrapolationException):
		distance=Twist()
		distance.linear.x=0
		distance.angular.z=0
		pub.publish(distance)
		pass
	rate.sleep()
