from gpiozero import Motor
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
left_motor = Motor(forward=12, backward=18, pwm=True, pin_factory=factory)
right_motor = Motor(forward=13, backward=19, pwm=True, pin_factory=factory)


def write_operation(operation, speed=0):

    match operation:
        case 'forward':
            left_motor.forward(speed)
            print('GOING FORWARD')
            right_motor.forward(speed)
            sleep(2)

        case 'backward':
            left_motor.backward(speed)
            print('GOING BACKWARDS')
            right_motor.backward(speed)
            sleep(2)

        case 'left':
            left_motor.backward(speed)
            print('GOING LEFT')
            right_motor.forward(speed)
            sleep(1)

        case 'right':
            left_motor.forward(speed)
            print('GOING RIGHT')
            right_motor.backward(speed)
            sleep(1)

        case 'stop':
            left_motor.stop(speed)
            right_motor.stop(speed)
