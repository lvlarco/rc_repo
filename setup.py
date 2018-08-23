import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class DriverMotor(object):
    '''Allows back wheels to go back and forth'''

    def __init__(self, in1_pin, in2_pin, driver_pin):
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin
        self.driver_pin = driver_pin

        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)
        GPIO.setup(self.driver_pin, GPIO.OUT)

    def clockwise(self):
        GPIO.output(self.in1_pin, True)    
        GPIO.output(self.in2_pin, False)
        GPIO.output(self.driver_pin, True)

    def counter_clockwise(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, True)
        GPIO.output(self.driver_pin, True)

    def driver_stop(self):
        GPIO.output(self.in1_pin, False)
        GPIO.output(self.in2_pin, False)
        GPIO.output(self.driver_pin, False)

class SteerMotor(object):
    '''Allows steering of forward wheels'''
 
    def __init__(self, servo_pin, frequency):
        self.servo_pin = servo_pin
        self.frequency = frequency

        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, self.frequency)
         
    def steer_right(self):
        self.pwm.start(15)
        #14 is neutral
         
    def steer_left(self):
        self.pwm.start(12)
        #14 is neutral
         
    def steer_stop(self):
        self.pwm.start(0)
