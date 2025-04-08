from config import *

class Utils:
    def __init__(self, robot):
        self.robot = robot
    
    def straight(self, distance, speed=SPEED):
        self.robot.base.reset()
        target_angle = self.robot.gyro.angle()
        p, i, d, error, last_error, pid = [0, 0, 0, 0, 0, 0]

        while abs(self.robot.base.distance()) < abs(distance):
            error = target_angle - self.robot.gyro.angle()
            
            # PID control
            p = error * DRIVE_Kp
            i += error * DRIVE_Ki
            d = DRIVE_Kd * (error - last_error)
            last_error = error
            
            # Clamp integral
            i = clamp(i, -DRIVE_I_MAX, DRIVE_I_MAX)

            pid = p + i + d
            #pid = self.clamp(pid, -100, 100)

            self.robot.base.drive(100, pid)
        self.robot.base.stop()
    
    def turn(self, angle, speed=SPEED_TURN):
        pass
    
### Separate util functions ###

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def debug(*args):
    if DEBUG:
        print(*args)