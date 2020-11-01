from Raspi_MotorHAT.Raspi_PWM_Servo_Driver import PWM
import atexit

class Servos:
    ## Constructor
    # @param[in] addr: the I2C address of the PWM chip.
    # @param[in] deflect_90_in_ms: set this to calibrate the seros
    #                               it is the deflection of 90 degrees 
    #                               in terms of pulse length in ms
    def __init__(self, addr=0x6f, deflect_90_in_ms = 0.9):
        self._pwm = PWM(addr)
        pwm_freqeuncy = 60 # this sets the timebase for the motorhat
        self._pwm.setPWMFreq(pwm_freqeuncy)

        #Frequency is 1/period, but working in ms, we can use 1000
        period_in_ms = 1000.0 / pwm_freqeuncy
        #the chip has 4096 steps in each period.
        pulse_steps = 4096.0 
        # mid point of the servo pulse length in milliseconds
        servo_mid_point_ms = 1.6
        # steps for every milisecond
        steps_per_ms = pulse_steps / period_in_ms
        # steps for a degree
        self.steps_per_degree = (deflect_90_in_ms * steps_per_ms) / 90.0
        # Mid point of the Servo in steps
        self.servo_mid_point_steps = servo_mid_point_ms * steps_per_ms

    def stop_all(self):
        # 0 in start is nothing, 4096 sets the OFF bit.
        self._pwm.setPWM(0, 0, 4096)
        self._pwm.setPWM(1, 0, 4096)
        self._pwm.setPWM(14, 0, 4096)
        self._pwm.setPWM(15, 0, 4096)
    
    def _convert_degrees_to_pwm(self, position):
        return int(self.servo_mid_point_steps + (position * self.steps_per_degree))

    ## Function to set the angle of a servo
    # @param[in] angle: the angle in degrees from the center. -90 to 90
    # @param[in] channel: channel of servo you wish to move
    def set_servo_angle(self, channel, angle):
        # validate angle
        if angle > 90 or angle < -90:
            raise ValueError("Angle outside of range")
        # Then set the position
        off_step = self._convert_degrees_to_pwm(angle)
        self._pwm.setPWM(channel, 0, off_step)