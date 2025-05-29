import RPi.GPIO as GPIO

const_frequency = 50
const_gpio_left_pin = 18
const_gpio_right_pin = 12
const_duty_cycle_discrete = 1

IS_INITIALIZED = False
left_pwm = None
right_pwm = None


def init_gpio():
    global IS_INITIALIZED, left_pwm, right_pwm

    if IS_INITIALIZED:
        return

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(const_gpio_left_pin, GPIO.OUT)
    GPIO.setup(const_gpio_right_pin, GPIO.OUT)

    left_pwm = GPIO.PWM(const_gpio_left_pin, const_frequency)
    right_pwm = GPIO.PWM(const_gpio_right_pin, const_frequency)
    left_pwm.start(0)
    right_pwm.start(0)

    IS_INITIALIZED = True


def pwm_control(pwm_obj, duty_cycle):
    pwm_obj.ChangeDutyCycle(duty_cycle)


def write_operation(operation, speed=1):
    global left_pwm, right_pwm
    init_gpio()

    dc = speed + const_duty_cycle_discrete

    match operation:
        case 'forward':
            print('GOING FORWARD')
            pwm_control(left_pwm, dc)
            pwm_control(right_pwm, dc)

        case 'backward':
            print('GOING BACKWARD')
            pwm_control(left_pwm, 0)
            pwm_control(right_pwm, 0)

        case 'left':
            print('TURNING LEFT')
            pwm_control(left_pwm, 0)
            pwm_control(right_pwm, dc)

        case 'right':
            print('TURNING RIGHT')
            pwm_control(left_pwm, dc)
            pwm_control(right_pwm, 0)

        case 'stop':
            print('STOPPING')
            pwm_control(left_pwm, 0)
            pwm_control(right_pwm, 0)
