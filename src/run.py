from pybricks.parameters import Color
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
    mv.straight(280)
    mv.turn(-90)
    mv.straight(55)
    # TODO: collect bolts
    mv.turn(135)
    mv.straight(420)
    mv.turn(-90)
    mv.straight(420)
    mv.turn(45)
    # TODO: release bolts
    mv.turn(90)
    mv.straight(350)
    # TODO: scan block
    mv.turn(90)
    mv.straight(150)
    mv.turn(-90)
    mv.straight(210)
    mv.turn(-90)
    mv.straight(775)
    mv.turn(-90)
    mv.straight(230)
    # TODO: grab hatch
    mv.straight(-230)
    # TODO: release hatch
    mv.turn(180)
    mv.until_color(Color.BLACK)
    mv.turn(-90)
    mv.line_follow(400)
    # TODO: collect nose parts
    mv.turn(-90)
