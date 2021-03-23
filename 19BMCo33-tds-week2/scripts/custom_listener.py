#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints

c = None
d = None
def callback(data):
	global c,d
	c = data.a
	d = data.b

	publisher()

def mat_op():
	e = c + d
	f = e * 100
	return e,f

def publisher():

	pub = rospy.Publisher("tl",two_ints,queue_size = 1)
	x,y = mat_op()
	r = rospy.Rate(1)
	msg = two_ints()
	while not rospy.is_shutdown():
		msg.a = x
		msg.b = y
		pub.publish(msg)
		#rospy.loginfo(y)
		r.sleep()

# if __name__ =="__main__":
# 	try:
# 		publisher()
# 	except rospy.ROSInterruptException:
# 		pass
def listener():
	rospy.init_node("two_ints_listener")
	rospy.Subscriber("two_ints",two_ints,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
