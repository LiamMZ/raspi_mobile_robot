import robot
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

def inc_pan_up(bot, pan):
    try:
        bot.set_pan(pan+10)
        return pan+10
    except ValueError as e:
        print("Angle out of range")
        return pan

def inc_pan_down(bot, pan):
    try:
        bot.set_pan(pan-10)
        return pan-10
    except ValueError as e:
        print("Angle out of range")
        return pan

def inc_tilt_up(bot, tilt):
    try:
        bot.set_tilt(tilt-10)
        return tilt-10
    except ValueError as e:
        print("Angle out of range")
        return tilt

def inc_tilt_down(bot, tilt):
    try:
        bot.set_tilt(tilt+10)
        return tilt+10
    except ValueError as e:
        print("Angle out of range")
        return tilt

if __name__=='__main__':
    bot = robot.Robot()
    tilt = 90
    pan = 0
    # bot.set_pan(pan)
    bot.set_tilt(tilt)
    while True:
        inp = input()
        if inp == 'w':
            straight(bot, 0)
        elif inp == 's':
            reverse(bot, 0)
        elif inp == 'a':
            spin_left(bot, 0)
        elif inp == 'd':
            spin_right(bot, 0)
        elif inp == 'pd':
            pan = inc_pan_down(bot, pan)
        elif inp == 'pu':
            pan = inc_pan_up(bot, pan)
        elif inp == 'td':
            tilt = inc_tilt_down(bot, tilt)
        elif inp == 'tu':
            tilt = inc_tilt_up(bot, tilt)
        else:
            stop(bot, 0)


