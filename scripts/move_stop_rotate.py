#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    # Lidar'ın 0. açısı robotun tam önüdür
    front_distance = msg.ranges[0]
    
    move_cmd = Twist()

    # Eğer öndeki engel 0.5 metreden uzaktaysa (veya sensör sonsuz değer okuyorsa)
    if front_distance > 0.5 or front_distance == float('inf'):
        move_cmd.linear.x = 0.2  # İleri doğru git
        move_cmd.angular.z = 0.0 # Dönme
    else:
        # Engel 0.5 metreden yakınsa
        move_cmd.linear.x = 0.0  # Dur
        move_cmd.angular.z = 0.5 # Kendi ekseninde dönerek engeli kurtar

    # Hız komutunu robota gönder
    pub.publish(move_cmd)

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance_node')
    
    # Hız komutlarını yayınlayacağımız (publish) kanal
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    # Lidar verilerini dinleyeceğimiz (subscribe) kanal
    sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
    
    rospy.loginfo("Engelden kacma kodu calisiyor. Robot harekete hazir.")
    rospy.spin()
