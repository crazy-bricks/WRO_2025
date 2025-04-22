#!/usr/bin/env pybricks-micropython
from config import *
from robot import Robot
from pose import Pose
from movement import Movement
from run import main_run

robot = Robot()
pose = Pose(0, 0, 0)
mv = Movement(robot, pose)

if __name__ == "__main__":
    main_run(robot, mv)
    raise SystemExit