from pybricks.parameters import Color, Button
from pybricks.tools import wait

from movement import Movement
from robot import Robot

from helper import debug_log
from config import *

def main_run(robot: Robot, mv: Movement):
    while True:
        pressed = robot.hub.buttons.pressed()
        if Button.CENTER in pressed:
            debug_log("button pressed, starting run", name="start")
            break

    robot.front_motor.reset_angle(0)
    robot.arm_motor.reset_angle(0)
    robot.base.reset()

    # Push yellow thingy
    mv.turn(45)
    mv.straight(290)
    mv.turn(45)
    mv.straight(660)
    mv.turn(-30)
    mv.straight(25)
    mv.straight(-25)
    mv.turn(30)
    mv.straight(310)
    # Grab red cable
    mv.turn(45)
    mv.straight(173)
    mv.turn(-45)
    mv.straight(315)
    mv.move_arm(pos="down")
    # Place red cable thingy
    mv.turn(-90)
    mv.straight(635)
    mv.turn(60)
    mv.straight(50)
    mv.move_arm(pos="up")
    mv.straight(40)
    mv.turn(-15)
    # Grab red thingy
    mv.straight(-250)
    mv.turn(-45)
    mv.straight(-180)
    mv.turn(-90)
    mv.straight(230)
    mv.turn(90)
    # Pull red thingy
    mv.rotate_arm(1)
    mv.move_arm(pos="down")
    mv.straight(-135, speed=SPEED_SLOW)
    mv.move_arm(pos="up")
    # Scan payload color
    mv.turn(-45)
    mv.straight(350)
    mv.turn(-45)
    mv.straight(130)
    payload_color = robot.side_color.color()
    debug_log("Payload color: {}".format(payload_color), name="payload")
    # Grab bob
    mv.straight(-130)
    mv.turn(-90)
    mv.straight(400)
    mv.move_arm(pos="down")
    # move bob
    mv.turn(90)
    mv.straight(1050)
    # Place bob
    mv.move_arm(pos="up")
    # Grab payload
    mv.straight(-50)
    mv.turn(90)
    mv.straight(200)
    mv.turn(-90)
    mv.straight(50)
    mv.move_arm(pos="down")
    mv.rotate_arm(PAYLOAD_ROTATION[payload_color])
    # Place payload
    mv.turn(90)
    mv.straight(100)
    mv.turn(90)
    mv.straight(400)
    mv.move_arm(pos="up")





    # mv.straight(350)
    # mv.turn(-90)
    # mv.straight(150)
    # mv.move_arm(pos="down")
    # mv.straight(11)



    # mv.straight(-100)
    # mv.turn(-30)
    # mv.straight(350)
    # mv.turn(-60)
    # mv.straight(200)
    
    # payload_color = robot.side_color.color()

    # mv.straight(-150)

    # mv.arm_up()
    # mv.turn(-45)
    # mv.straight(220)








