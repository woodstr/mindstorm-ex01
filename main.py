#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
import time
from star_wars_music import *
from vader import *

if __name__ == "__main__":
    # Initialize the EV3 brick.
    ev3 = EV3Brick()

    # Wheel parameters
    circumf = 25.5 # circumference of the wheels in cm
    l_port = Port.C
    r_port = Port.B

    # go forward 90cm
    forward(
        circumf=circumf,
        distance=90, # 90cm
        speed=200,
        l_port=l_port, r_port=r_port,
        wait=False
    )

    # beep imperial march p1
    beep_imperial_p1(ev3)
    time.sleep(4)

    spot_turn(
        circumf=circumf,
        turn_degrees=30,
        wheel_dist=9, # 9cm
        speed=-200,
        l_port=l_port,
        r_port=r_port
    )

    forward(
        circumf=circumf,
        distance=45, # 45cm
        speed=200,
        l_port=l_port, r_port=r_port,
        wait=False
    )

    beep_imperial_p2(ev3)
    time.sleep(3)

    # end beep
    ev3.speaker.set_speech_options(
        language='en-us',
        voice='m7',
        speed=100,
        pitch=0,
    )
    ev3.speaker.set_volume(100)
    ev3.speaker.say('If you only knew the power of the dark side.')