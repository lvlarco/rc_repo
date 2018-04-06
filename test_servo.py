import RPi.GPIO as GPIO
from time import sleep

servo_pin = 18
frequency = 50
duty = 10

GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, frequency)

pwm.start(0)
pwm.ChangeDutyCycle(duty)

sleep(3)
pwm.stop()

GPIO.cleanup()