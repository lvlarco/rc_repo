import RPi.GPIO as GPIO
#import rover as rover
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 12

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(button_pin)
    if input_state == False:
        print'Going Forward'
        
        sleep(0.2)
