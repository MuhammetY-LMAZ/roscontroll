#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class SimplePID:
    def __init__(self):
        rospy.init_node('pid_controller_node')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # PID Katsayıları (Bunları simülasyonda deneyerek ayarlaman gerekir)
        self.Kp = 1.0  # Hatayla orantılı tepki
        self.Ki = 0.0  # Geçmiş hataların birikimi
        self.Kd = 0.1  # Hatanın değişim hızı (gelecek tahmini)

        self.error = 0.0
        self.prev_error = 0.0
        self.integral = 0.0

    def compute_velocity(self, setpoint, current_value):
        # 1. Hatayı hesapla (Hedef - Mevcut Durum)
        self.error = setpoint - current_value
        
        # 2. İntegrali hesapla (Hataları topla)
        self.integral += self.error
        
        # 3. Türevi hesapla (Mevcut hata - Bir önceki hata)
        derivative = self.error - self.prev_error
        
        # 4. PID Formülü
        output = (self.Kp * self.error) + (self.Ki * self.integral) + (self.Kd * derivative)
        
        # Bir sonraki döngü için hatayı kaydet
        self.prev_error = self.error
        
        return output

    def run(self):
        rate = rospy.Rate(10) # 10 Hz
        move_cmd = Twist()
        
        while not rospy.is_shutdown():
            # Örnek Kullanım: Robotun düz gitme hızını PID ile ayarlamak.
            # Normalde 'current_value' sensörden okunur (örn. odometri).
            # Burada mantığı kurman için temsili değerler verilmiştir.
            
            hedef_hiz = 0.5 
            mevcut_hiz = 0.0 # Sensörden okuduğunu varsay
            
            # PID'den çıkış al
            kontrol_sinyali = self.compute_velocity(hedef_hiz, mevcut_hiz)
            
            # Hızı sınırlandır (çok yüksek hız vermemek için)
            move_cmd.linear.x = max(min(kontrol_sinyali, 0.22), -0.22) 
            
            self.pub.publish(move_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        pid = SimplePID()
        pid.run()
    except rospy.ROSInterruptException:
        pass
