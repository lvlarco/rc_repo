import RPi.GPIO as GPIO
from rover import Motor
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 12

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button_pin)
    if input_state == False:
        Motor.forward()
        print'Going Forward'
        
        sleep(0.2)
