#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import time
from star_wars_music import *
from vader import *
from pybricks.ev3devices import Motor, ColorSensor, InfraredSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import random
import pickle as pkl
import os

os.system('setfont Lat15-TerminusBold14')
# os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font

logs = {'action': [], 'decision': [], 'l_sensor': [], 'r_sensor': []}

# Function to read the light sensor values and make a decision
def follow_line(DRIVE_SPEED):
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()

    # log values
    logs['action'].append('follow_line')
    logs['l_sensor'].append(left_value)
    logs['r_sensor'].append(right_value)

    # >= / <= used to avoid missing equals case

    # if left white, right white: go straight
    if left_value >= THRESHOLD and right_value >= THRESHOLD:
        robot.drive(DRIVE_SPEED, 0)
        logs['decision'].append('straight')

    # if left black, right white: turn left
    elif left_value <= THRESHOLD and right_value >= THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)
        logs['decision'].append('left')

    # if left white, right black: turn right
    elif left_value >= THRESHOLD and right_value <= THRESHOLD:
        robot.drive(DRIVE_SPEED, -TURN_RATE)
        logs['decision'].append('right')

    # if left black, right black: stop (intersection)
    elif left_value <= THRESHOLD and right_value <= THRESHOLD:
        robot.stop()
        logs['decision'].append('stop (intersection)')

    # SHOULD EVER GET HERE
    else:
        robot.stop()
        print('WTF')
        logs['decision'].append('stop (wtf)')

def detect_intersection():
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()

    # log values
    logs['action'].append('detect_intersection')
    logs['l_sensor'].append(left_value)
    logs['r_sensor'].append(right_value)

    # intersection if all black
    if left_value < THRESHOLD and right_value < THRESHOLD:
        logs['decision'].append('intersection')
        return True
    
    # no intersection
    logs['decision'].append('no intersection')
    return False

# need to change based on planner
def navigate_intersection(instruction):
    wait(1000)
    if instruction == 'straight':
        robot.straight(-100)
    elif instruction == 'left':
        robot.turn(90)
    elif instruction == 'right':
        robot.turn(-90)
    wait(1000)

    # checks for if sensors are still on intersection?
    while True:
        if not detect_intersection():
            break
        print('still on intersection! HELP!')
        time.sleep(10)
    return


if __name__ == "__main__":

    # Initialize motors
    left_motor = Motor(Port.C)
    right_motor = Motor(Port.B)

    # Initialize light sensors
    left_sensor = ColorSensor(Port.S4)
    right_sensor = ColorSensor(Port.S1)

    # DriveBase setup: Assuming the robot is 12 cm wide and the wheels have a 5.6 cm diameter.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=81.169, axle_track=255)

    # Adjusted Threshold
    THRESHOLD = 10
    DRIVE_SPEED = -50
    TURN_RATE = 10

    # Instruction list
    instructions = ['left', 'right', 'straight']
    print('EV3 Python Starts!')
    while instructions:
        if detect_intersection():
            instruction = instructions.pop(0)
            navigate_intersection(instruction)
        else:
            follow_line(DRIVE_SPEED)

    # debug only
    # forward(12, 10, 500, l_port=Port.A, r_port=Port.C, wait=True)
    
    # print logs since filesaving goes to ev3
    # print(logs['decision'])