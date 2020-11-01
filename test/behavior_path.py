import src.robot
from Raspi_MotorHAT import Raspi_MotorHAT
import sys
from time import sleep

def straight(bot, seconds):
    bot.set_left(80)
    bot.set_right(80)
    sleep(seconds)

def reverse(bot, seconds):
    bot.set_left(-80)
    bot.set_right(-80)
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

def spin_right(bot, seconds):
    bot.set_left(80)
    bot.set_right(-80)
    sleep(seconds)

def stop(bot, seconds):
    bot.set_left(0)
    bot.set_right(0)
    sleep(seconds)

if __name__=='__main__':
    bot = robot.Robot()
    while True:
        inp = raw_input()
        if inp == 'w':
            straight(bot, 0)
        elif inp == 's':
            reverse(bot, 0)
        elif inp == 'a':
            spin_left(bot, 0)
        elif inp == 'd':
            spin_right(bot, 0)
        else:
            stop(bot, 0)


