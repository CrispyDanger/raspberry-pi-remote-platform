from .gpio_setup import left_pwm, right_pwm

const_frequency = 50
const_gpio_left_pin = 18
const_gpio_right_pin = 12
const_duty_cycle_discrete = 1


def pwm_control(pwm_obj, duty_cycle):
    pwm_obj.ChangeDutyCycle(duty_cycle)


def write_operation(operation, speed=1):
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
