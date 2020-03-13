from microbit import *
import microbit
import superbit
import neopixel

k = 0
flag = 2
display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)

def limit_change():
    global flag
    if microbit.button_a.is_pressed():
        superbit.motor_control(superbit.M1, -255, 0)
        flag = 0
        display.show(Image.ARROW_S)

    elif microbit.button_b.is_pressed():
        superbit.motor_control(superbit.M1, 255, 0)
        flag = 1
        display.show(Image.ARROW_N)

while True:
    limit_change()
    if flag == 1:
        while k < 255:
            np[0] = (k, 0, 0)
            np[1] = (k, 0, 0)
            np[2] = (k, 0, 0)
            np[3] = (k, 0, 0)
            np.show()
            k += 1
            np.clear()

        else:
            np[0] = (k, 0, 0)
            np[1] = (k, 0, 0)
            np[2] = (k, 0, 0)
            np[3] = (k, 0, 0)
            np.show()
            k = 255 - k
            np.clear()