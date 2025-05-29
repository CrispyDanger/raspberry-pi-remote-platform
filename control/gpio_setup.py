import RPi.GPIO as GPIO

const_frequency = 50
const_gpio_left_pin = 18
const_gpio_right_pin = 12
const_duty_cycle_discrete = 1

left_pwm = None
right_pwm = None
initialized = False


def init_gpio():
    global left_pwm, right_pwm, initialized

    if initialized:
        return  # prevent double init

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(const_gpio_left_pin, GPIO.OUT)
    GPIO.setup(const_gpio_right_pin, GPIO.OUT)

    left_pwm = GPIO.PWM(const_gpio_left_pin, const_frequency)
    right_pwm = GPIO.PWM(const_gpio_right_pin, const_frequency)

    left_pwm.start(0)
    right_pwm.start(0)

    initialized = True
    print("GPIO initialized")
