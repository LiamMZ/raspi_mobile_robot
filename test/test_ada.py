import time
from adafruit_motorkit import MotorKit

kit = MotorKit(address=0x6f)

kit.motor4.throttle = 1.0

time.sleep(0.5)
kit.motor4.throttle = 0
