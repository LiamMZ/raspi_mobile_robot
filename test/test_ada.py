import time
from adafruit_motorkit import MotorKit

kit = MotorKit(address=0x6f)

kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
kit.motor3.throttle = 1.0
kit.motor4.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0
kit.motor2.throttle = .0
kit.motor3.throttle = .0
kit.motor4.throttle = .0