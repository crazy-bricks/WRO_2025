#!/usr/bin/env pybricks-micropython
from config import *
from robot import Robot
from pose import Pose
from utils import Utils
from run import main_run

robot = Robot()
pose = Pose(0, 0, 0)
utils = Utils(robot, pose)

if __name__ == "__main__":
    main_run(robot, utils)
    raise SystemExit