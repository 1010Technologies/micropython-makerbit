from microbit import *
from makerbit import *

display.show("M")
sleep(2000)
display.off()

u1 = Ultrasonic(pin5, pin8)
u2 = Ultrasonic(pin15, pin14)

while True:
    d1 = u1.get_distance()
    d2 = u2.get_distance()
    if d1 > 20:
        print("1: " + str(d1))
    if d2 > 20:
        print("2: " + str(d2))
