from pybricks.tools import wait, StopWatch
from config import *
from helper import clamp, debug_log

class Movement:
    def __init__(self, robot, pose):
        self.robot = robot
        self.pose = pose
    
    def straight(self, distance, speed=SPEED, target_angle=None, timeout=None):
        self.robot.base.reset()

        if target_angle is None:
            target_angle = self.pose.angle
        self.pose.set_angle(target_angle)

        direction = 1 if distance > 0 else -1

        timer = StopWatch()

        while abs(distance) > abs(self.robot.base.distance()):
            error = target_angle - self.robot.gyro.angle()
            
            # PID control
            p = error * PID_DRIVE["kp"]
            i += error * PID_DRIVE["ki"]
            d = (error - last_error) * PID_DRIVE["kd"]
            last_error = error
            
            # Clamp integral
            i = clamp(i, -PID_DRIVE["i_max"], PID_DRIVE["i_max"])

            correction = p + i + d
            #correction = clamp(correction, -100, 100)

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached")
                break
        self.robot.base.stop()
    
    def turn(self, angle, speed=SPEED_TURN, tolerance=TURN_TOLERANCE, timeout=None):
        target_angle = self.pose.angle + angle
        error = target_angle - self.robot.gyro.angle()

        timer = StopWatch()

        while abs(error) > tolerance:
            error = target_angle - self.robot.gyro.angle()
            debug_log(error)

            # PID control
            p = error * PID_TURN["kp"]
            i += error * PID_TURN["ki"]
            d = (error - last_error) * PID_TURN["kd"]
            last_error = error

            # Clamp integral
            i = clamp(i, -PID_TURN["i_max"], PID_TURN["i_max"])
            
            correction = p + i + d

            self.robot.base.drive(0, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Turn timeout reached")
                break
        self.robot.base.stop()
        self.pose.set_angle(target_angle)

    def follow_line(self, distance=100, speed=SPEED):
        self.robot.base.reset()

        while abs(self.robot.base.distance()) < distance:
            left = self.robot.left_color.reflection()
            right = self.robot.right_color.reflection()
            error = left - right
            correction = error * PID_COLOR["kp"]
            self.robot.base.drive(speed, correction)
        self.robot.base.stop()
    
    def reset_gyro(self):
        wait(250)
        self.robot.gyro.reset_angle(0)
        self.pose.reset_angle()
        wait(250)
