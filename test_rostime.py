#coding=utf-8  
import rospy

        
if __name__ == '__main__':
    rospy.init_node('test_rostime_node', anonymous=True)
    # r = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown():
    #     print("hello")
    #     # now = rospy.get_rostime()
    #     # print(now)
    #     r.sleep()


    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        rate.sleep()
    # print(rospy.Time.now())
    rospy.spin()
