from pybricks.parameters import Color, Button
from pybricks.tools import wait

from helper import debug_log
from config import *

def main_run(robot, mv):
    if not DEBUG:
        while robot.hub.buttons.pressed() is []:
            pass

    robot.front_motor.reset_angle(0)
    robot.arm_motor.reset_angle(0)
    robot.base.reset()

    mv.turn(45)
    mv.straight(365)
    mv.turn(45)
    mv.straight(900)
    mv.turn(45)
    mv.straight(200)
    mv.turn(-45)
    mv.straight(380)
    mv.move_arm(pos="down")
    mv.turn(-90)
    mv.straight(620)
    mv.turn(45)
    mv.straight(100)
    mv.move_arm(pos="up")
    mv.straight(-200)
    mv.turn(-45)
    mv.straight(-230)
    mv.turn(-90)
    mv.straight(320)
    mv.turn(90)
    mv.move_arm(pos="down")
    mv.straight(-130)
    mv.move_arm(pos="up")
    mv.arm_up()
    mv.turn(-45)
    mv.straight(220)



    return


    return
    while True:
        pressed = robot.hub.buttons.pressed()
        if Button.RIGHT in pressed:
            robot.front_motor.run_angle(SPEED_TURN, 90)
        if Button.LEFT in pressed:
            robot.front_motor.run_angle(SPEED_TURN, -90)


"""
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
"""