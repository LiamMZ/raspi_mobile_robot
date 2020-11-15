import time
from adafruit_servokit import ServoKit

kit = ServoKit(address=0x6f, channels=8, frequency=90)
print(kit.continuous_servo)
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.continuous_servo[1].throttle = -1
time.sleep(1)
kit.continuous_servo[1].throttle = 0