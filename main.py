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

    print('LEFT: ', left_value)
    print('RIGHT: ', right_value)

    # log values
    logs['action'].append('follow_line')
    logs['l_sensor'].append(left_value)
    logs['r_sensor'].append(right_value)

    difference = left_value - right_value

    # if sensor values below threshold, stop (intersection)
    if left_value <= THRESHOLD and right_value <= THRESHOLD:
        robot.stop()
        logs['decision'].append('stop (intersection)')
        return True

    # turn left (left sensor more black)
    elif difference < 0:
        robot.drive(DRIVE_SPEED, TURN_RATE)
    # turn right (right sensor more black)
    elif difference > 0:
        robot.drive(DRIVE_SPEED, -TURN_RATE)
    # keep last direction
    else:
        print('Continue with last drive function')
    
    return False

# need to change based on planner
def navigate_intersection(instruction):
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()
    difference = left_value - right_value

    time.sleep(1)
    if instruction == 'straight':
        robot.straight(-100)
    elif instruction == 'left':
        robot.straight(-50)
        robot.turn(65)
        robot.straight(-50)
        while True:
            robot.turn(5)
            if abs(difference) < 5:
                break
    elif instruction == 'right':
        robot.straight(-50)
        robot.turn(-65)
        robot.straight(-50)
        while True:
            robot.turn(-5)
            if abs(difference) < 5:
                break
    elif instruction == 'back':
        go_back()
    time.sleep(1)

    # checks for if sensors are still on intersection?
    # while True:
    #     if not detect_intersection():
    #         break
    #     print('still on intersection! HELP!')
    #     time.sleep(2)

    return

def go_back():
    # TODO: back up, 180 turn, go back to intersection

    robot.straight(140)
    robot.turn(140)
    robot.straight(70)
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
    THRESHOLD = 4
    DRIVE_SPEED = -50
    TURN_RATE = 10

    # Instruction list
    instructions = ['left', 'left', 'left', 'left', 'straight', 'straight', 'back']
    print('EV3 Python Starts!')

    while instructions:
        intersection = follow_line(DRIVE_SPEED)
        if intersection:
            instruction = instructions.pop(0)
            navigate_intersection(instruction)

    # debug only
    # forward(12, 10, 500, l_port=Port.A, r_port=Port.C, wait=True)
    
    # print logs since filesaving goes to ev3
    # print(logs['decision'])