#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
import time
from star_wars_music import *
from vader import *
from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait
from pybricks.ev3devices import InfraredSensor

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

# Function to read the light sensor values and make a decision
def follow_line():
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()
    middle_value = middle_sensor.reflection()

    # Line following logic based on sensor values
    if left_value < THRESHOLD and right_value > THRESHOLD: # 
        robot.drive(DRIVE_SPEED, -TURN_RATE)
    elif right_value < THRESHOLD and left_value > THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)
    elif middle_value < THRESHOLD:
        robot.drive(DRIVE_SPEED, 0)
    else:
        robot.stop()

def detect_intersection():
    left_value = left_sensor.reflection()
    right_value = right_sensor.reflection()
    middle_value = middle_sensor.reflection()

    # Detect if all sensors detect black (indicating a cross intersection)
    if left_value < THRESHOLD and right_value < THRESHOLD and middle_value < THRESHOLD:
        return True
    return False


if __name__ == "__main__":

    # Initialize motors
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    # Initialize light sensors
    left_sensor = ColorSensor(Port.S1)
    middle_sensor = ColorSensor(Port.S2)
    right_sensor = ColorSensor(Port.S3)

    # DriveBase setup: Assuming the robot is 12 cm wide and the wheels have a 5.6 cm diameter.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=8.1169, axle_track=120)

    # Adjusted Threshold
    THRESHOLD = 10
    DRIVE_SPEED = -20
    TURN_RATE = 20

    # Main loop
    while True:
        follow_line()

        if detect_intersection():
            robot.turn(90)
            wait(1000)



'''
    # Initialize the EV3 brick.
    ev3 = EV3Brick()

    # Wheel parameters
    circumf = 25.5 # circumference of the wheels in cm
    l_port = Port.C
    r_port = Port.B

    # Initialize the sensor.
    sensor = ColorSensor(Port.S4)

    

    while True:
        # Read the color and reflection
        color = sensor.color()
        reflection = sensor.reflection()

        # Print the measured color and reflection.
        print(color, reflection)

        # Move the sensor around and see how
        # well you can detect colors.

        # Wait so we can read the value.
        wait(1000)
'''

'''
reflection observation: 
black color cause a low reflection reading, increasing the angles cause a lower 
reflection reading, and more light is causing better reflection reading. 
'''