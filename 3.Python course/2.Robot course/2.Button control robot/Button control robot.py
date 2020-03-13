from microbit import *

import microbit
import superbit

display.show(Image.HAPPY)
superbit.motor_control(superbit.M1, 0, 0)

while True:
    if microbit.button_a.is_pressed():
        superbit.motor_control(superbit.M1, 255, 0)
    if microbit.button_b.is_pressed():
        superbit.motor_control(superbit.M1, -255, 0)
