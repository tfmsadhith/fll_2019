#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
import math

tank = MoveTank('outA', 'outB')
ext_a = MediumMotor('outC')

# note that medium motors are being used.

center_radius = 6.5
radius = 4.5 
perimeter = 2 * math.pi * radius

def move_cm(dist, s):
    degrees_to_go = (dist / perimeter) * 360
    tank.on_for_degrees(s, s, degrees_to_go)
    
def left_turn(deg, s):
    degrees_to_go = (2 * deg * math.pi * center_radius / perimeter)
    tank.on_for_degrees(-s - 10, s, degrees_to_go)

def right_turn(deg, s):
    degrees_to_go = (2 * deg * math.pi * center_radius / perimeter)
    tank.on_for_degrees(s - 10, -s, degrees_to_go)

# swing
move_cm(-130, 30)
ext_a.on_for_degrees(100, -90)
move_cm(-20, 30)
# swing done!

# building
ext_a.on_for_degrees(50,90)
move_cm(20,30)
ext_a.on_for_degrees(50, 90)
move_cm(-20,30)
right_turn(100,50)
ext_a.on_for_degrees(100, -90)
left_turn(30,50)
move_cm(20,30)
left_turn(60,30)

ext_a.on_for_degrees(85,60)
move_cm(-100,70)