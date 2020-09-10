import robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep

def straight(bot, seconds):
    bot.set_left(80)
    bot.set_right(80)
    sleep(seconds)

def turn_left(bot, seconds):
    bot.set_left(20)
    bot.set_right(80)
    sleep(seconds)

def turn_right(bot, seconds):
    bot.set_left(80)
    bot.set_right(20)
    sleep(seconds)

def spin_left(bot, seconds):
    bot.set_left(-80)
    bot.set_right(80)
    sleep(seconds)

if __name__=='__main__':
    bot = robot.Robot()
    # straight(bot, 1)
    # turn_right(bot, 1)
    # straight(bot, 1)
    # turn_left(bot, 1)
    # straight(bot, 1)
    # turn_left(bot, 1)
    # straight(bot, 1)
    # spin_left(bot, 1)
    spin_left(bot, 5)


