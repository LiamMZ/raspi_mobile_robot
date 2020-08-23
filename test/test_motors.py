from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

mh = Raspi_MotorHAT(addr=0x6f)

lmb = mh.getMotor(1)
lmf = mh.getMotor(2)
rmf = mh.getMotor(3)
rmb = mh.getMotor(4)

def turn_off_motors():
    lmb.run(Raspi_MotorHAT.RELEASE)
    lmf.run(Raspi_MotorHAT.RELEASE)
    rmf.run(Raspi_MotorHAT.RELEASE)
    rmb.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

lmb.setSpeed(150)
lmf.setSpeed(150)
rmb.setSpeed(150)
rmf.setSpeed(150)

lmf.run(Raspi_MotorHAT.FORWARD)
lmb.run(Raspi_MotorHAT.FORWARD)
rmb.run(Raspi_MotorHAT.FORWARD)
rmf.run(Raspi_MotorHAT.FORWARD)
time.sleep(1)
