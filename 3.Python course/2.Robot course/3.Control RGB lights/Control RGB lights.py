from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HAPPY)

while True:
    np.clear()
    np[0] = (255, 0, 0)
    np[1] = (255, 0, 0)
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    np.show()
    sleep(1000)

    np.clear()
    np[0] = (0, 255, 0)
    np[1] = (0, 255, 0)
    np[2] = (0, 255, 0)
    np[3] = (0, 255, 0)
    np.show()
    sleep(1000)

    np.clear()
    np[0] = (0, 0, 255)
    np[1] = (0, 0, 255)
    np[2] = (0, 0, 255)
    np[3] = (0, 0, 255)
    np.show()
    sleep(1000)
