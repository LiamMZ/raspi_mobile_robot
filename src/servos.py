from adafruit_servokit import ServoKit
import atexit

class Servos:
    ## Constructor
    # @param[in] addr: the I2C address of the PWM chip.
    # @param[in] deflect_90_in_ms: set this to calibrate the seros
    #                               it is the deflection of 90 degrees 
    #                               in terms of pulse length in ms
    def __init__(self, addr=0x6f, deflect_90_in_ms = 0.9):
        self.kit = ServoKit(address=addr, channels=8)

        self._pwm = self.kit.continuous_servo
    
    def _convert_degrees_to_pwm(self, position):
        return float(position/90)

    ## Function to set the angle of a servo
    # @param[in] angle: the angle in degrees from the center. -90 to 90
    # @param[in] channel: channel of servo you wish to move
    def set_servo_angle(self, channel, angle):
        # validate angle
        if angle > 90 or angle < 0:
            raise ValueError("Angle outside of range")
        # Then set the position
        off_step = self._convert_degrees_to_pwm(angle)
        self._pwm[channel].throttle = off_step