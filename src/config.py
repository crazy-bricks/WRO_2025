from pybricks.parameters import Port


############## ROBOT ##############

PORT_RIGHT_MOTOR = Port.B
PORT_LEFT_MOTOR = Port.A
PORT_GYRO = Port.S1
PORT_COLOR_LEFT = Port.S2
PORT_COLOR_RIGHT = Port.S3


# TODO: change testing values
WHEEL_DIAMETER = 37  # mm
AXLE_TRACK = 120     # mm

############## SETTINGS ##############

PID_DRIVE = {
    "kp": 10,
    "ki": 0,
    "kd": 0,
    "i_max": 100
}

PID_TURN = {
    "kp": 5,
    "ki": 0.2,
    "kd": 1,
    "i_max": 100
}

PID_COLOR = {
    "kp": 1
}

SPEED = 300
SPEED_TURN = 200

TURN_TOLERANCE = 2  # degrees

DEBUG = True