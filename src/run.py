from helper import debug_log
from config import *

def main_run(robot, mv):
    mv.turn(45)
    mv.straight(270)
    mv.turn(-45)
    mv.straight(540)
    mv.turn(45)
    # TODO: raise first flag
    mv.turn(-135)
    mv.straight(300)
    mv.turn(90)
