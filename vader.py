from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction

def calc_degrees(circumf, distance):
    '''
    Calculate degrees to turn based on wheel circumference and distance to move forward.
    E.g. if circumference of wheel is 20cm and distance to move forward is 40cm, then the wheels need to turn 2 rotations.
    '''
    rotations = distance/circumf
    degrees = rotations*360
    return degrees

def forward(circumf, distance, speed, l_port, r_port, wait=True):
    '''
    Move the robot forward a certain distance
     - circumf: circumference of the wheels
     - distance: distance to move forward
     - l_port/r_port: left and right motor ports
     - wait: whether to wait for the motors to finish moving
    
    Degrees to turn is calculated based on wheel circumference and distance to move forward.
    E.g. if circumference of wheel is 20cm and distance to move forward is 40cm, then the wheels need to turn 2 rotations.
    '''

    right_motor = Motor(r_port, positive_direction=Direction.CLOCKWISE)
    left_motor = Motor(l_port, positive_direction=Direction.CLOCKWISE)

    degrees = calc_degrees(circumf, distance)

    left_motor.run_angle(speed, degrees, wait=False)
    right_motor.run_angle(speed, degrees, wait=wait)

    return

def turn(circumf, distance, speed, port, wait=True):
    '''
    Turn with other wheel(s) stationary

     - circumf: circumference of the wheels
     - distance: distance to move forward (cm)
     - speed: speed to turn the wheels (degrees/second)
     - port: motor port to turn
     - wait: whether to wait for the motors to finish moving
    '''

    motor = Motor(port, positive_direction=Direction.CLOCKWISE)

    degrees = calc_degrees(circumf, distance)

    motor.run_angle(speed, degrees, wait=wait)

    return

def arc_len_calc(central_angle, radius):
    '''
    Calculate the arc length based on the central angle and radius of the circle.
    '''
    return (central_angle*radius) * (3.14159/180)

def spot_turn(circumf, turn_degrees, wheel_dist, speed, l_port, r_port, wait=True):
    '''
    Perform a turn on the spot

     - circumf: circumference of the wheels
     - turn_degrees: degrees to turn
     - wheel_dist: distance between the wheels
     - speed: speed to turn the wheels (degrees/second)
     - l_port/r_port: left and right motor ports
     - wait: whether to wait for the motors to finish moving
    '''

    turn_degrees = turn_degrees * 2 # double the turn degrees to account for spot turn

    left_motor = Motor(l_port, positive_direction=Direction.CLOCKWISE)
    right_motor = Motor(r_port, positive_direction=Direction.CLOCKWISE)

    # calculate degrees to turn
    circumf_to_spin = arc_len_calc(turn_degrees, wheel_dist)
    degrees = calc_degrees(circumf, circumf_to_spin)

    left_motor.run_angle(speed, degrees, wait=False)
    right_motor.run_angle(-speed, degrees, wait=wait)

    return