#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import Pose2D
rospy.init_node('node_listener') #init node
listener = tf.TransformListener()
rate = rospy.Rate(10.0) #set spin rate to 10 Hz
pub = rospy.Publisher('rover_current_pose', Pose2D, queue_size=1)
while not rospy.is_shutdown():
#lookup for the newest transform
	try:
		(trans,rot)=listener.lookupTransform('/odom', '/base_link',
		rospy.Time(0))
		#get euler angles form quaternions
		euler =tf.transformations.euler_from_quaternion(rot)
		#print translation and rotation
		print 'pos: ',trans
		print '########'
		posithion=Pose2D()
		posithion.x=trans[0]
		posithion.y=trans[1]
		pub.publish(posithion)
		
	except (tf.LookupException, tf.ConnectivityException,
	tf.ExtrapolationException):
		pass
	
	rate.sleep()
