from microbit import *
from makerbit import *

motor_a = Motor(Motor.A)
motor_b = Motor(Motor.B)

while True:
    print("START")

    print("Motor A and B at different speed")
    sleep(1000)
    motor_a.run(30)
    motor_b.run(100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B forward, Motor A forward")
    sleep(1000)
    motor_a.run(100)
    motor_b.run(100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B forward, Motor A stopped")
    sleep(1000)
    motor_b.run(100)
    motor_a.stop()
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B forward, Motor A reverse")
    sleep(1000)
    motor_a.run(-100)
    motor_b.run(100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B stopped, Motor A forward")
    motor_a.run(100)
    motor_b.stop()
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B reverse, Motor A forward")
    sleep(1000)
    motor_a.run(100)
    motor_b.run(-100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B reverse, Motor A stopped")
    sleep(1000)
    motor_a.stop()
    motor_b.run(-100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("Motor B reverse, Motor A reverse")
    sleep(1000)
    motor_a.run(-100)
    motor_b.run(-100)
    sleep(2000)
    motor_a.stop()
    motor_b.stop()

    print("END")
    sleep(3000)
