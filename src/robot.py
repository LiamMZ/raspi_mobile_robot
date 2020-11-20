from adafruit_motorkit import MotorKit
from servos import Servos
import atexit

class Robot(object):
    def __init__(self, motorhat_addr=0x6f):
        # set up motorhat with address parameter
        self.kit = MotorKit(address=motorhat_addr)

        # get local variable for each motor
        self.left_motor_rear = self.kit.motor1
        self.left_motor_front = self.kit.motor2
        self.right_motor_rear = self.kit.motor3
        self.right_motor_front = self.kit.motor4

        # make sure motors stop when code exits
        atexit.register(self.stop_motors)

        # Set up servo motors for pan and tilt
        self.servos = Servos(addr=motorhat_addr)
    
    # convert speed from 0-100 to robot speeds
    def convert_speed(self, speed):
        #Scale the speed
        output_speed = speed/100
        return output_speed

    # release motors
    def stop_motors(self):
        self.left_motor_rear.throttle = 0.0
        self.right_motor_rear.throttle= 0.0
        self.left_motor_front.throttle = 0.0
        self.right_motor_front.throttle = 0.0
    
    # sets speeds of left wheels
    def set_left(self, speed):
        output_speed = self.convert_speed(speed)
        self.left_motor_rear.throttle = output_speed
        self.left_motor_front.throttle = output_speed
        
    
    # sets speeds of right wheels
    def set_right(self, speed):
        output_speed = self.convert_speed(speed)
        self.right_motor_rear.throttle = output_speed
        self.right_motor_front.throttle = output_speed

    def move(self, speed):
        self.set_left(speed)
        self.set_right(speed)
    
    def set_pan(self, angle):
        self.servos.set_servo_angle(1, angle)

    def set_tilt(self, angle):
        self.servos.set_servo_angle(0,angle)
        
    def stop_all(self):
        self.stop_motors()

        # Reset the servos
        # self.servos.stop_all()

