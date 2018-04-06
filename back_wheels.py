import RPi.GPIO as GPIO
from rover import Motor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

forward_pin = 12
backward_pin = 26
left_in1_pin = 4
left_in2_pin = 17
right_in1_pin = 23
right_in2_pin = 24
enable_pin = 18
frequency = 1000
duty_cycle = 50

GPIO.setup(forward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(backward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
left_motor = Motor(left_in1_pin, left_in2_pin, enable_pin, frequency, duty_cycle)
right_motor = Motor(right_in1_pin, right_in2_pin, enable_pin, frequency, duty_cycle)

while True:
	forward_state = GPIO.input(forward_pin)
	backward_state = GPIO.input(backward_pin)

	if forward_state == False:
		left_motor.clockwise()
		right_motor.counter_clockwise()
		print'Going Forward'
		sleep(0.1)
	if forward_state == True:
		left_motor.stop()
		right_motor.stop()
		
	if backward_state == False:
		left_motor.counter_clockwise()
		right_motor.clockwise()
		print'Going Backward'
		sleep(0.1)
	if backward_state == True:
		left_motor.stop()
		right_motor.stop()

GPIO.cleanup()
