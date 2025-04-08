from pybricks.parameters import Port


############## ROBOT ##############

PORT_RIGHT_MOTOR = Port.B
PORT_LEFT_MOTOR = Port.A
PORT_GYRO = Port.S1
PORT_COLOR_LEFT = Port.S2
PORT_COLOR_RIGHT = Port.S3

WHEEL_DIAMETER = 56  # mm
AXLE_TRACK = 100     # mm TODO: edit this value

############## SETTINGS ##############

PID_DRIVE = {
    "kp": 5,
    "ki": 0,
    "kd": 0,
    "i_max": 100
}

PID_TURN = {
    "kp": 5,
    "ki": 0,
    "kd": 0,
    "i_max": 100
}

SPEED = 300
SPEED_TURN = 200

TURN_TOLERANCE = 2  # degrees

DEBUG = True