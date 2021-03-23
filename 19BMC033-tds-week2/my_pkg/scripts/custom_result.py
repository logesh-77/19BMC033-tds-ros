#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints
g = None
def callback(data):
	global g
	g = data.b
	rospy.loginfo('the new output is %d' %g )
def listener():
	rospy.init_node("result")
	rospy.Subscriber("tl",two_ints,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
