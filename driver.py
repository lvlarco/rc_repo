import RPi.GPIO as GPIO
from rover import DriverMotor
from time import sleep

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
servo_pin = 18
# frequency = 1000
# duty_cycle = 50

GPIO.setup(forward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(backward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left_motor = DriverMotor(left_in1_pin, left_in2_pin, driver_pin)
right_motor = DriverMotor(right_in1_pin, right_in2_pin, driver_pin)
steer_motor = SteerMotor(servo_pin)

while True:
	forward_state = GPIO.input(forward_pin)
	backward_state = GPIO.input(backward_pin)
	
	right_state = GPIO.input(turn_right_pin)
	left_state = GPIO.input(turn_left_pin)

	#Driver
	if forward_state == False:
		left_motor.clockwise()
		right_motor.counter_clockwise()
		print'Going Forward'
		sleep(0.1)
	if forward_state == True:
		left_motor.driver_stop()
		right_motor.driver_stop()
		
	if backward_state == False:
		left_motor.counter_clockwise()
		right_motor.clockwise()
		print'Going Backward'
		sleep(0.1)
	if backward_state == True:
		left_motor.driver_stop()
		right_motor.driver_stop()
	
	#Steering
	if right_state == False:
		steer_motor.steer_right()
		print'Turning Right'
		sleep(0.1)
	if forward_state == True:
		steer_motor.steer_stop()
		
	if right_state == False:
		steer_motor.steer_left()
		print'Turning Left'
		sleep(0.1)
	if forward_state == True:
		steer_motor.steer_stop()

GPIO.cleanup()
