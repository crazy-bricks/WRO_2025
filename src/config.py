from pybricks.parameters import Port, Color


##############  ROBOT  ##############

PORT_RIGHT_MOTOR = Port.B
PORT_LEFT_MOTOR = Port.C
PORT_FRONT_MOTOR = Port.A
PORT_ARM_MOTOR = Port.D

PORT_GYRO = Port.S1
PORT_COLOR_LEFT = Port.S2
PORT_COLOR_RIGHT = Port.S3
PORT_COLOR_SIDE = Port.S4

WHEEL_DIAMETER = 62.4 # mm
AXLE_TRACK = 164     # mm (168 og)

ARM_POSITION = {
    "up": 0,
    "mid": -1100,
    "down": -2200
}

PAYLOAD_ROTATION = {
    Color.RED: 0,
    Color.GREEN: 2,
    Color.BLUE: -1,
    Color.YELLOW: 1,
}

##############  PID  ##############

PID_DRIVE = {
    "kp": 4.5,
    "ki": 0.01,
    "kd": 0.01,
    "i_max": 100,
    "output_max": None
}

PID_TURN = {
    "kp": 1,
    "ki": 0,
    "kd": 0,
    "i_max": 100,
    "output_max": 100
}

PID_COLOR = {
    "kp": 1
}

##############  MOVEMENT  ##############

SPEED = 300         # mm/s
SPEED_SLOW = 100    # mm/s
SPEED_LINE = 200    # mm/s

SPEED_ARM = 1200    # deg/s
SPEED_TURN = 600    # deg/s

TURN_TOLERANCE = 2  # degrees

ACCEL_RATIO = 0.2
DECEL_RATIO = 0.2

##############  MISC  ##############

DEBUG = True