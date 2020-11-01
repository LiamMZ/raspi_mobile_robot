from Raspi_MotorHAT import Raspi_MotorHAT
from servos import Servos
import atexit

class Robot(object):
    def __init__(self, motorhat_addr=0x6f):
        # set up motorhat with address parameter
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)

        # get local variable for each motor
        self.left_motor_rear = self._mh.getMotor(1)
        self.left_motor_front = self._mh.getMotor(2)
        self.right_motor_rear = self._mh.getMotor(4)
        self.right_motor_front = self._mh.getMotor(3)

        # make sure motors stop when code exits
        atexit.register(self.stop_motors)

        # Set up servo motors for pan and tilt
        self.servos = Servos(addr=motorhat_addr)
    
    # convert speed from 0-100 to robot speeds
    def convert_speed(self, speed):
        # choose the running mode 
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        
        #Scale the speed
        output_speed = (abs(speed)*255)/100
        return mode, output_speed

    # release motors
    def stop_motors(self):
        self.left_motor_rear.run(Raspi_MotorHAT.RELEASE)
        self.right_motor_rear.run(Raspi_MotorHAT.RELEASE)
        self.left_motor_front.run(Raspi_MotorHAT.RELEASE)
        self.right_motor_front.run(Raspi_MotorHAT.RELEASE)
    
    # sets speeds of left wheels
    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor_rear.setSpeed(output_speed)
        self.left_motor_front.setSpeed(output_speed)
        self.left_motor_rear.run(mode)
        self.left_motor_front.run(mode)
        
    
    # sets speeds of right wheels
    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor_rear.setSpeed(output_speed)
        self.right_motor_front.setSpeed(output_speed)
        self.right_motor_rear.run(mode)
        self.right_motor_front.run(mode)

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
        self.servos.stop_all()

