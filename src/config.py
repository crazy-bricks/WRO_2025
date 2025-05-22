from pybricks.parameters import Port


############## ROBOT ##############

PORT_RIGHT_MOTOR = Port.A
PORT_LEFT_MOTOR = Port.B
PORT_FRONT_MOTOR = Port.C
PORT_ARM_MOTOR = Port.D
PORT_GYRO = Port.S1
PORT_COLOR_LEFT = Port.S2
PORT_COLOR_RIGHT = Port.S3
PORT_COLOR_SIDE = Port.S4

WHEEL_DIAMETER = 62.4 # mm
AXLE_TRACK = 168     # mm

ARM_POSITION = {
    "up": 0,
    "mid": -1060,
    "down": -2120
}

##############  PID  ##############

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

ACCEL_RATIO = 0.2
DECEL_RATIO = 0.2

DEBUG = True