import RPi.GPIO as GPIO
from rover import Motor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 12
left_in1_pin = 4
left_in2_pin = 17
right_in1_pin = 23
right_in2_pin = 24
Motor1E = 18

#__motor_ = Motor()

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button_pin)
    left_motor = Motor(left_in1_pin, left_in2_pin)
    right_motor = Motor(right_in1_pin, right_in2_pin)
    
    if input_state == False:
        left_motor.clockwise()
        right_motor.counter_clockwise()
        print'Going Forward'
        
        sleep(0.2)
