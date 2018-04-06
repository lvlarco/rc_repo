import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

servo_pin = 18
frequency = 100
duty = 5
x=0
turn_right_pin = 13
turn_left_pin = 19

GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(turn_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(turn_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm = GPIO.PWM(servo_pin, frequency)

pwm.start(0)

while 1:
	pwm.ChangeDutyCycle(x)
	if(GPIO.input(turn_right_pin) == False):
		if(x<25):
			x=x+1
			print x
			sleep(0.2)
	if(GPIO.input(turn_left_pin) == False):
		if(x>0):
			x=x-1
			print x
			sleep(0.2)


GPIO.cleanup()
