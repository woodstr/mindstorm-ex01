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

logs = {'action': [], 'decision': [], 'l_sensor': [], 'm_sensor': [], 'r_sensor': []}

# Function to read the light sensor values and make a decision
def follow_line():
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()
    middle_value = middle_sensor.reflection()

    # log values
    logs['action'].append('follow_line')
    logs['l_sensor'].append(left_value)
    logs['m_sensor'].append(middle_value)
    logs['r_sensor'].append(right_value)

    # Line following logic based on sensor values

    # if middle black, left white, right white: go straight
    if middle_value < THRESHOLD and left_value > THRESHOLD and right_value > THRESHOLD:
        robot.drive(DRIVE_SPEED, 0)
        logs['decision'].append('straight')

    # if middle black, left black, right white: turn left
    elif middle_value < THRESHOLD and left_value < THRESHOLD and right_value > THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)
        logs['decision'].append('left')

    # if middle white, left black, right white: turn left
    elif middle_value > THRESHOLD and left_value < THRESHOLD and right_value > THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)
        logs['decision'].append('left')

    # if middle black, left white, right black: turn right
    elif middle_value < THRESHOLD and right_value < THRESHOLD and left_value > THRESHOLD:
        robot.drive(DRIVE_SPEED, -TURN_RATE)
        logs['decision'].append('right')

    # if middle white, left white, right black: turn right
    elif middle_value > THRESHOLD and left_value > THRESHOLD and right_value < THRESHOLD:
        robot.drive(DRIVE_SPEED, -TURN_RATE)
        logs['decision'].append('right')

    # if middle white, left black, right black: stop (intersection without straight)
    elif middle_value > THRESHOLD and right_value < THRESHOLD and left_value < THRESHOLD:
        robot.stop()
        logs['decision'].append('stop (intersection without straight)')

    # if all sensors white: go forward (slow)
    elif left_value > THRESHOLD and right_value > THRESHOLD and middle_value > THRESHOLD:
        robot.drive(-5, 0)
        logs['decision'].append('forward (slow)')

    # if all sensors black: stop (intersection with straight?)
    elif left_value < THRESHOLD and right_value < THRESHOLD and middle_value < THRESHOLD:
        robot.stop()
        logs['decision'].append('stop (all black)')

    # if left black, right black, middle white: stop (T junction)
    elif left_value < THRESHOLD and right_value < THRESHOLD and middle_value > THRESHOLD:
        robot.stop()
        logs['decision'].append('stop (T junction)')

    # idk
    else:
        robot.stop()
        logs['decision'].append('stop (idk)')

def detect_intersection():
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()
    middle_value = middle_sensor.reflection()

    # log values
    logs['action'].append('detect_intersection')
    logs['l_sensor'].append(left_value)
    logs['m_sensor'].append(middle_value)
    logs['r_sensor'].append(right_value)

    # all black: 4 way intersection
    if left_value < THRESHOLD and right_value < THRESHOLD and middle_value < THRESHOLD:
        logs['decision'].append('4-way')
        return '4-way'
    
    # left black, right black, middle white: T junction
    elif left_value < THRESHOLD and right_value < THRESHOLD and middle_value > THRESHOLD:
        logs['decision'].append('T-junction')
        return 'T-junction'
    
    # left black, middle black, right white: L left
    elif left_value < THRESHOLD and middle_value < THRESHOLD and right_value > THRESHOLD:
        logs['decision'].append('L-left')
        return 'L-left'
    
    # left white, middle black, right black: L right
    elif left_value > THRESHOLD and middle_value < THRESHOLD and right_value < THRESHOLD:
        logs['decision'].append('L-right')
        return 'L-right'
    
    # no intersection
    return False

def navigate_intersection(intersection):
    # if 4 way, pick left, right, or straight
    if intersection == '4-way':
        decision = random.choice(['left', 'right', 'straight'])

        if decision == 'left':
            robot.drive(DRIVE_SPEED, 90)
        elif decision == 'right':
            robot.drive(DRIVE_SPEED, -90)
        elif decision == 'straight':
            robot.drive(DRIVE_SPEED, 0)
    
    # if T junction, pick left or right
    elif intersection == 'T-junction':
        decision = random.choice(['left', 'right'])
        if decision == 'left':
            robot.drive(DRIVE_SPEED, 90)
        elif decision == 'right':
            robot.drive(DRIVE_SPEED, -90)
    
    # if L left or L right, turn
    elif intersection == 'L-left':
        robot.straight(-50)
        turnNinetyDeg(robot)
    elif intersection == 'L-right':
        robot.drive(DRIVE_SPEED, -90)


def turnNinetyDeg(robot: DriveBase):
    robot.turn(12.5) # Make no sense, but, set to 12.5, the robot turns 90 degrees.

if __name__ == "__main__":

    # Initialize motors
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.C)

    # Initialize light sensors
    left_sensor = ColorSensor(Port.S1)
    middle_sensor = ColorSensor(Port.S2)
    right_sensor = ColorSensor(Port.S3)

    # DriveBase setup: Assuming the robot is 12 cm wide and the wheels have a 5.6 cm diameter.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=81.169, axle_track=255)

    # Adjusted Threshold
    THRESHOLD = 10
    DRIVE_SPEED = 5
    TURN_RATE = 10

    # Main loop
    count = 0 
    while True:
        if count == 1:
            break

        # determine if we are at an intersection
        intersection = detect_intersection()

        # navigate intersection if exists
        if intersection:
            navigate_intersection(intersection)
            count += 1
            wait(2000) # buffer time to let us realise the decision
        else:
            # no intersection just follow the line
            follow_line()

    # forward(12, 10, 500, l_port=Port.A, r_port=Port.C, wait=True)
    
    # print logs since filesaving goes to ev3
    print(logs)