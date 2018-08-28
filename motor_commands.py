import RPi.GPIO as GPIO
from setup import DriverMotor
from setup import SteerMotor
from time import sleep
from bluedot import BlueDot
from signal import pause

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Input pins
forward_pin = 12
backward_pin = 26
turn_right_pin = 13
turn_left_pin = 19
#Output pins
left_in1_pin = 4
left_in2_pin = 17
right_in1_pin = 23
right_in2_pin = 24
driver_pin = 18
servo_pin = 16
frequency = 100
# duty_cycle = 50

GPIO.setup(forward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(backward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(turn_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(turn_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left_motor = DriverMotor(left_in1_pin, left_in2_pin, driver_pin)
right_motor = DriverMotor(right_in1_pin, right_in2_pin, driver_pin)
steer_motor = SteerMotor(servo_pin, frequency)

def dpad(pos):
    if pos.top:
        left_motor.clockwise()
        right_motor.counter_clockwise()
        print'Going Forward'
        sleep(0.1)
    elif pos.bottom:
        left_motor.counter_clockwise()
        right_motor.clockwise()
        print'Going Backward'
        sleep(0.1)
    elif pos.left:
        steer_motor.steer_left()
        print'Turning Left'
        sleep(0.2)
    elif pos.right:
        steer_motor.steer_right()
        print'Turning Right'
        sleep(0.2)
    elif pos.middle:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
def release(pos):
    if pos.top:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
        sleep(0.1)
    elif pos.bottom:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
        sleep(0.1)
    elif pos.left:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
        sleep(0.2)
    elif pos.right:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
        sleep(0.2)
    elif pos.middle:
        left_motor.driver_stop()
        right_motor.driver_stop()
        steer_motor.steer_stop()
        print("Stop")
    
    
bd = BlueDot()
bd.when_pressed = dpad
bd.when_released = release
pause()