import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from time import sleep
 
left_in1_pin = 17
left_in2_pin = 4
right_in1_pin = 23
right_in2_pin = 24
Motor1E = 18

#Left motor
GPIO.setup(left_in1_pin,GPIO.OUT)
GPIO.setup(left_in2_pin,GPIO.OUT)

#Right motor
GPIO.setup(right_in1_pin,GPIO.OUT)
GPIO.setup(right_in2_pin,GPIO.OUT)

GPIO.setup(Motor1E,GPIO.OUT)
 
#print "Turning left motor on"
GPIO.output(left_in1_pin,GPIO.HIGH)
GPIO.output(left_in2_pin,GPIO.LOW)
#GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)

print "Stopping motor"
GPIO.output(left_in1_pin,GPIO.LOW)
GPIO.output(left_in2_pin,GPIO.LOW)
#GPIO.output(Motor1E,GPIO.LOW)
"""
print "Turning right motor on"
GPIO.output(right_in1_pin,GPIO.HIGH)
GPIO.output(right_in2_pin,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)

print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
"""
 
GPIO.cleanup()
