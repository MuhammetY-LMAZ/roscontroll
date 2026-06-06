# ROS Kontrol Ödevi: Engelden Kaçma ve PID Kontrolcü

Bu depo, ROS Noetic ortamında TurtleBot3 simülasyonu kullanılarak gerçekleştirilen temel robotik kontrol ve navigasyon görevlerini içermektedir. Proje kapsamında Lidar sensörü ile çevresel farkındalık oluşturulmakta ve PID kontrol algoritması ile hız referansları hesaplanmaktadır.

## 📋 Proje İçeriği ve Görevler

Bu paket (`control_odevi`) altında iki temel görev icra edilmektedir:

1. **Move-Stop-Rotate (Engelden Kaçma):** Robotun `/scan` konusundan (topic) alınan Lidar lazer okumaları değerlendirilmektedir. Ön kısımdaki engeller 0.5 metre mesafeden sürekli olarak taranmakta, engel tespit edildiğinde robot durdurularak kendi ekseni etrafında dönüş manevrası uygulanmaktadır.
   * **İlgili Script:** `move_stop_rotate.py`

2. **PID Kontrolcü (PID Controller):**
   Sistem dinamiği göz önüne alınarak bir PID (Proportional-Integral-Derivative) kontrolcü tasarımı gerçekleştirilmektedir. Tanımlanan hedef hıza ulaşabilmek adına güncel hata hesaplanmakta ve belirlenen Kp, Ki, Kd katsayıları üzerinden doğrusal hız komutları oluşturulmaktadır.
   * **İlgili Script:** `pid_controller.py`

## 🛠️ Gereksinimler

Sistemin çalıştırılabilmesi için aşağıdaki yazılım ve paketler kullanılmaktadır:
* Ubuntu 20.04 & ROS Noetic
* Python 3.x
* `turtlebot3_gazebo` ve `turtlebot3_msgs` paketleri

## 🚀 Kurulum ve Derleme

Çalışma alanına (workspace) paketin eklenmesi ve derlenmesi için aşağıdaki adımlar izlenmektedir:

```bash
# Çalışma alanının kaynak dizinine geçiş yapılmaktadır
cd ~/catkin_ws/src

# Depo klonlanmaktadır
git clone [https://github.com/KULLANICI_ADIN/ros_control_odevi.git](https://github.com/KULLANICI_ADIN/ros_control_odevi.git)

# Python dosyalarına çalıştırma izni verilmektedir
cd ros_control_odevi/scripts
chmod +x move_stop_rotate.py pid_controller.py

# Paket derlenmekte ve çalışma alanı güncellenmektedir
cd ~/catkin_ws
catkin_make
source devel/setup.bash
