import time
import math
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
from multiprocessing import Lock, Process, Value

class IMUOdometry:
    def __init__(self, mutex, x = 0.0, y=0.0, theta=0.0):
        self.x = Value('d', x) 
        self.y = Value('d', y)
        self.theta = Value('d', theta)
        self.mutex = mutex
        self.vx = 0
        self.omega = 0
        self.imu = MPU9250(address_ak=AK8963_ADDRESS, 
                            address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
                            address_mpu_slave=None, 
                            bus=1,
                            gfs=GFS_1000, 
                            afs=AFS_8G, 
                            mfs=AK8963_BIT_16, 
                            mode=AK8963_MODE_C100HZ)

        self.imu.configure() # Apply the settings to the registers.
        self.p = Process(target=self.calc_odom)
        self.p.start()

    def __str__(self):
        with self.mutex:
            output =  f"""
                    Position: [{self.x} {self.y} {self.theta}]\n\n
                    Velocity: [{self.vx} {self.omega}]
                """
        return output

    def calc_odom(self):
        while True:
            start_time = time.time()
            start_acc = self.convert_to_mps2(self.imu.readAccelerometerMaster()[0])
            start_omega = self.convert_to_radps(self.imu.readGyroscopeMaster()[2])
            time.sleep(.25)
            acc = (start_acc + self.convert_to_mps2(self.imu.readAccelerometerMaster()[0]))/2
            omega = (start_omega + self.convert_to_radps(self.imu.readGyroscopeMaster()[2]))/2
            time_diff = time.time()-start_time
            with self.mutex:
                self.vx += (acc * time_diff)
                self.omega += (omega * time_diff)
                self.update_position(self.vx, self.omega, time_diff)

    ## Function to convert from g to m/s^2
    # @param[in] acc - aray of accelerations [ax, ay, az] in units of g
    # @returns converted_acc - array of accelerations in units of m/s^2
    def convert_to_mps2(self, acc):
        return acc/9.80665
    
    def convert_to_radps(self, w):
        return (w*math.pi)/180

    def update_position(self, vx, w, t):
        theta = (self.theta + (self.theta+(w*t)))/2
        self.theta += (w*t)
        self.x += vx*math.cos(theta)
        self.y += vx*math.sin(theta)
        print(self.x, self.y, self.theta)
    
    def  x(self):
        return shared

if __name__=="__main__":
    mutex = Lock()
    odom = IMUOdometry(mutex)
    while True:
        print(odom)
        time.sleep(1)