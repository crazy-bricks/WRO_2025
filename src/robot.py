from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.robotics import DriveBase

from config import *

class Robot:
    def __init__(self):
        """
        Initializes the Robot class
        """
        self.hub = EV3Brick()
        self.right_motor = Motor(PORT_RIGHT_MOTOR)
        self.left_motor = Motor(PORT_LEFT_MOTOR)
        self.base = DriveBase(self.left_motor, self.right_motor, WHEEL_DIAMETER, AXLE_TRACK)
        self.gyro = GyroSensor(PORT_GYRO)
        self.left_color = ColorSensor(PORT_COLOR_LEFT)
        self.right_color = ColorSensor(PORT_COLOR_RIGHT)