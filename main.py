#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
import time

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

# Play a sound.
# beep to the star wars theme song
# ev3.speaker.beep(440, 500)
# ev3.speaker.beep(440, 500)
# ev3.speaker.beep(440, 500)
# ev3.speaker.beep(349, 350)
# ev3.speaker.beep(523, 150)
# ev3.speaker.beep(440, 500)
# ev3.speaker.beep(349, 350)
# ev3.speaker.beep(523, 150)
# ev3.speaker.beep(440, 1000)
# ev3.speaker.beep(659, 500)
# ev3.speaker.beep(659, 500)
# ev3.speaker.beep(659, 500)
# ev3.speaker.beep(698, 350)
# ev3.speaker.beep(523, 150)
# ev3.speaker.beep(415, 500)
# ev3.speaker.beep()

# circumference cirka 22cm
# 1 rotation = 22cm
# for moving forward 90cm, need to rotate 90/22 = 4.09 rotations

# move forward 90cm simultaneously
def forward(circumf):
    right_motor = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
    left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)

    left_motor.run_angle(500, 4.09*360, wait=False)
    right_motor.run_angle(500, 4.09*360)

time.sleep(5)

for i in range(2):
    left_motor.run_angle(500, 4.09*360, wait=False)
    right_motor.run_angle(500, 4.09*360)


# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
# left_motor.run_target(500, 90)
# right_motor.run_target(500, 90)


# Play another beep sound.
# ev3.speaker.beep(1000, 500)