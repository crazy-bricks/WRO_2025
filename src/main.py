#!/usr/bin/env pybricks-micropython
from config import *
from robot import Robot
from utils import Utils
from run import main_run

robot = Robot()
utils = Utils(robot)

if __name__ == "__main__":
    main_run(robot, utils)
    raise SystemExit