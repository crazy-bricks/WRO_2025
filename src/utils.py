from pybricks.tools import wait
from config import *

class Utils:
    def __init__(self, robot, pose):
        self.robot = robot
        self.pose = pose
    
    def straight(self, distance, speed=SPEED, target_angle=None):
        self.robot.base.reset()
        p, i, d, error, last_error, pid = [0, 0, 0, 0, 0, 0]

        if target_angle is None:
            target_angle = self.pose.angle
        

        while abs(self.robot.base.distance()) < abs(distance):
            error = target_angle - self.robot.gyro.angle()
            
            # PID control
            p = error * PID_DRIVE["kp"]
            i += error * PID_DRIVE["ki"]
            d = (error - last_error) * PID_DRIVE["kd"]
            last_error = error
            
            # Clamp integral
            i = clamp(i, -PID_DRIVE["i_max"], PID_DRIVE["i_max"])

            pid = p + i + d
            #pid = self.clamp(pid, -100, 100)

            self.robot.base.drive(100, pid)
        self.robot.base.stop()
    
    def turn(self, angle, speed=SPEED_TURN):
        pass

    def follow_line(self, speed=SPEED):
        pass
    
    def reset_gyro(self):
        wait(250)
        self.robot.gyro.reset_angle(0)
        self.pose.reset_angle()
        wait(250)
    
### Separate util functions ###

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def debug(*args):
    if DEBUG:
        print(*args)