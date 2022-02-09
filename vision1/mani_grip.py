#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def manipulator_control():
    rospy.init_node('manipulator_control') 
    motor_1 = rospy.Publisher('/vision1/motor1_ctrl/command', Float64, queue_size=10)
    motor_2 = rospy.Publisher('/vision1/motor2_ctrl/command', Float64, queue_size=10)
    motor_3 = rospy.Publisher('/vision1/motor3_ctrl/command', Float64, queue_size=10)
    
    rate = rospy.Rate(1) 
    rospy.loginfo("Data is being sent")  
    while not rospy.is_shutdown():
        twist = Float64()

        #Initial pose
        twist.data = 90 * 0.01744
        motor_1.publish(twist)
        twist.data = 90 * 0.01744
        motor_2.publish(twist)
        twist.data = 0 * 0.01744
        motor_3.publish(twist)
        
        rate.sleep()

        #picking pose
        twist.data = 0 * 0.01744
        motor_1.publish(twist)
        twist.data = 0 * 0.01744
        motor_2.publish(twist)
        twist.data = -90 * 0.01744
        motor_3.publish(twist)

        rate.sleep()
        twist.data = 0 * 0.01744
        motor_1.publish(twist)
        twist.data = 0 * 0.01744
        motor_2.publish(twist)
        twist.data = -90 * 0.01744
        motor_3.publish(twist)

        rate.sleep()
        twist.data = 90 * 0.01744
        motor_1.publish(twist)
        twist.data = 0 * 0.01744
        motor_2.publish(twist)
        twist.data = -90 * 0.01744
        motor_3.publish(twist)
        

if __name__ == '__main__':
    try:
        manipulator_control()
    except rospy.ROSInterruptException: 
        pass
