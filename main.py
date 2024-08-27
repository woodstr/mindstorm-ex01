#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
import time
from star_wars_music import beep_imperial_march
import asyncio

# helpers
def forward(circumf, distance, l_port, r_port):
    '''
    Move the robot forward a certain distance
     - circumf: circumference of the wheels
     - distance: distance to move forward
    
    Degrees to turn is calculated based on wheel circumference and distance to move forward.
    E.g. if circumference of wheel is 20cm and distance to move forward is 40cm, then the wheels need to turn 2 rotations.
    '''

    right_motor = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
    left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

    rotations = distance/circumf
    degrees = rotations*360

    left_motor.run_angle(500, degrees, wait=False)
    right_motor.run_angle(500, degrees)

    return

if __name__ == "__main__":
    # Initialize the EV3 brick.
    ev3 = EV3Brick()

    # beep to the star wars theme song
    beep_imperial_march(ev3)

    # go forward 90cm
    forward(
        circumf=22, # cirka 22cm
        distance=90, # 90cm
        l_port=Port.B, r_port=Port.C
    )

    # turn left 45cm

    # point at an angle relatively to the starting direction of 30 degrees

    # end beep
    ev3.speaker.say('Luke, I am your father')