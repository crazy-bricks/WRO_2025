from pybricks.tools import wait, StopWatch
from config import *
from helper import clamp, debug_log

class Movement:
    def __init__(self, robot, pose):
        """
        Initializes the Movement class
        :param robot: Robot object
        :param pose: Pose object
        """
        self.robot = robot
        self.pose = pose
    
    def straight(self, distance, speed=SPEED, target_angle=None, timeout=None):
        """
        Drives the robot straight

        :param distance: Distance to drive in mm
        :param speed: Speed to drive at in mm/s
        :param target_angle: Angle to drive at in degrees
        :param timeout: Timeout in miliseconds
        :return: None
        """
        self.robot.base.reset()
        p, i, d, correction, error, last_error = [0] * 6

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

            debug_log("error", error, "correction", correction, "p", p, "i", i, "d", d)

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached")
                break
        self.robot.base.stop()
    
    def straight_ramp(self, distance, min_speed=SPEED_SLOW, max_speed=SPEED,  target_angle=None, timeout=None):
        """
        Drives the robot straight with acceleration and deceleration
        
        :param distance: Distance to drive in mm
        :param min_speed: Minimum speed to drive at in mm/s
        :param max_speed: Maximum speed to drive at in mm/s
        :param target_angle: Angle to drive at in degrees
        :param timeout: Timeout in miliseconds
        :return: None
        """
        if min_speed > max_speed:
            return

        self.robot.base.reset()
        p, i, d, correction, error, last_error = [0] * 6

        if target_angle is None:
            target_angle = self.pose.angle
        self.pose.set_angle(target_angle)

        direction = 1 if distance > 0 else -1

        timer = StopWatch()

        accel_thresh = 0.2 * abs(distance) # accel -> coast
        decel_thresh = 0.2 * abs(distance) # coast -> decel
        speed = min_speed

        while abs(distance) > abs(self.robot.base.distance()):
            error = target_angle - self.robot.gyro.angle()
            
            ### PID control ###
            p = error * PID_DRIVE["kp"]
            i += error * PID_DRIVE["ki"]
            d = (error - last_error) * PID_DRIVE["kd"]
            last_error = error
            
            # Clamp integral
            i = clamp(i, -PID_DRIVE["i_max"], PID_DRIVE["i_max"])

            correction = p + i + d
            #correction = clamp(correction, -100, 100)

            debug_log("error", error, "correction", correction, "p", p, "i", i, "d", d)

            ### Speed ramping ###
            acceleration = (max_speed - min_speed) / (accel_thresh)
            deceleration = (min_speed - max_speed) / (distance - decel_thresh)

            if abs(self.robot.base.distance()) < accel_thresh:
                # accelerate
                speed = min_speed + acceleration * abs(self.robot.base.distance())
            elif abs(self.robot.base.distance()) > decel_thresh:
                # decelerate
                speed = max_speed + deceleration * (abs(self.robot.base.distance()) - decel_thresh)
            else:
                # coast
                speed = max_speed

            self.robot.base.drive(direction * speed, correction)

            if timeout is not None and timer.time() > timeout:
                debug_log("Drive timeout reached")
                break
        self.robot.base.stop()

    def turn(self, angle, speed=SPEED_TURN, tolerance=TURN_TOLERANCE, timeout=None):
        """
        Turns the robot by a given angle
        
        :param angle: Angle to turn in degrees
        :param speed: Speed to turn at in deg/s
        :param tolerance: Turn tolerance in degrees
        :param timeout: Timeout in milliseconds
        :return: None
        """
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
        """
        Drive a set distance while following a line

        :param distance: Distance to drive in mm
        :param speed: Speed to drive at in mm/s
        :return: None
        """
        self.robot.base.reset()

        while abs(self.robot.base.distance()) < distance:
            left = self.robot.left_color.reflection()
            right = self.robot.right_color.reflection()
            error = left - right
            correction = error * PID_COLOR["kp"]
            self.robot.base.drive(speed, correction)
        self.robot.base.stop()
    
    def until_color(self, color, speed=SPEED):
        """
        Drive until a color is detected
        
        :param color: Color to detect
        :param speed: Speed to drive at in mm/s
        :return: None
        """
        while True:
            left = self.robot.left_color.color()
            right = self.robot.right_color.color()
            if left == color or right == color:
                break
            self.straight(100, speed)
        self.robot.base.stop()

    def reset_gyro(self):
        """
        Resets the gyro angle and the pose angle
        :return: None
        """
        wait(250)
        self.robot.gyro.reset_angle(0)
        self.pose.reset_angle()
        wait(250)
