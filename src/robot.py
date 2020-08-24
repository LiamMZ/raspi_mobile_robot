from Raspi_MotorHAT import Raspi_MotorHAT
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
    
    # release motors
    def stop_motors(self):
        self.left_motor_rear.run(Raspi_MotorHAT.RELEASE)
        self.right_motor_rear.run(Raspi_MotorHAT.RELEASE)
        self.left_motor_front.run(Raspi_MotorHAT.RELEASE)
        self.right_motor_front.run(Raspi_MotorHAT.RELEASE)

    def forward(self):
        self.left_motor_rear.run(Raspi_MotorHAT.FORWARD)
        self.right_motor_rear.run(Raspi_MotorHAT.FORWARD)
        self.left_motor_front.run(Raspi_MotorHAT.FORWARD)
        self.right_motor_front.run(Raspi_MotorHAT.FORWARD)

