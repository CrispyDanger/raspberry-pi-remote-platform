from gpiozero import Motor
from time import sleep


def write_operation(operation, speed):
    left_motor = Motor(forward=12, backward=13, pwm=True)
    right_motor = Motor(forward=18, backward=19, pwm=True)

    match operation:
        case 'forward':
            left_motor.forward(speed)
            right_motor.forward(speed)
            sleep(2)

        case 'backward':
            left_motor.backward(speed)
            right_motor.backward(speed)
            sleep(2)

        case 'left':
            left_motor.backward(speed)
            right_motor.forward(speed)
            sleep(1)

        case 'right':
            left_motor.forward(speed)
            right_motor.backward(speed)
            sleep(1)

        case 'stop':
            left_motor.stop()
            right_motor.stop()
