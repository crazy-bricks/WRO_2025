from pybricks.parameters import Port


############## ROBOT ##############

PORT_RIGHT_MOTOR = Port.C
PORT_LEFT_MOTOR = Port.B
PORT_FRONT_MOTOR = Port.A
PORT_GYRO = Port.S1
PORT_COLOR_LEFT = Port.S2
PORT_COLOR_RIGHT = Port.S3

WHEEL_DIAMETER = 56 # mm
AXLE_TRACK = 96     # mm

############## PID ##############

PID_DRIVE = {
    "kp": 6,
    "ki": 0,
    "kd": 2,
    "i_max": 100,
    "output_max": None
}

PID_TURN = {
    "kp": 5,
    "ki": 0.2,
    "kd": 1,
    "i_max": 100,
    "output_max": None
}

PID_COLOR = {
    "kp": 1
}

SPEED = 300         # mm/s
SPEED_SLOW = 100    # mm/s
SPEED_LINE = 200    # mm/s

SPEED_TURN = 200    # deg/s
TURN_TOLERANCE = 2  # degrees

DEBUG = True