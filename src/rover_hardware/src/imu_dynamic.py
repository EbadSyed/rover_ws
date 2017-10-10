#!/usr/bin/env python
import rospy
import tf
import math
br = tf.TransformBroadcaster()
cnt = 0
position_rover = [0.,0.]
def callback(data):
	imu_msg.header.stamp = rospy.get_rostime()
	imu_msg.header.frame_id = "imu"
	imu_msg.orientation.x=data.quat_x
	imu_msg.orientation.y=data.quat_y
	imu_msg.orientation.z=data.quat_z
	imu_msg.orientation.w=data.quat_w
	
	imu_msg.angular_velocity.x = data.gyro_x
	imu_msg.angular_velocity.y = data.gyro_y
	imu_msg.angular_velocity.z = data.gyro_z
	imu_msg.linear_acceleration.x = data.acc_x
	imu_msg.linear_acceleration.y = data.acc_y
	imu_msg.linear_acceleration.z = data.acc_z
	br.sendTransform((position_rover[0], position_rover[1],0),
		tf.transformations.quaternion_from_euler(r,p,y),
		rospy.Time.now(), "base_footprint", "attitude")

rospy.Subscriber("/imu_data", ImuMin, callback)

if __name__ == '__main__':
	rospy.init_node("dynamic_tf_broadcaster")
	rate = rospy.Rate(100)
	while not rospy.is_shutdown():
		#getting actual position
		#broadcasting transform
		
		rate.sleep()
