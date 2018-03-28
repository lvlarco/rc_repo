import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
left_in1_pin = 4
left_in2_pin = 17
right_in1_pin = 23
right_in2_pin = 24
Motor1E = 18

class Motor(object):
        def __init__(self, in1_pin, in2_pin):
                self.in1_pin = in1_pin
                self.in2_pin = in2_pin
               
                GPIO.setup(self.in1_pin, GPIO.OUT)
                GPIO.setup(self.in2_pin, GPIO.OUT)
       
        def clockwise(self):
                GPIO.output(self.in1_pin, True)    
                GPIO.output(self.in2_pin, False)
        def counter_clockwise(self):
                GPIO.output(self.in1_pin, False)
                GPIO.output(self.in2_pin, True)
               
        def stop(self):
                GPIO.output(self.in1_pin, False)    
                GPIO.output(self.in2_pin, False)
                
try:
    
    right_motor = Motor(right_in1_pin, right_in2_pin)
    left_motor = Motor(left_in1_pin, left_in2_pin)

    print "Left Clockwise"
    left_motor.clockwise()
    sleep(2)
    print "Left CC"
    left_motor.counter_clockwise()
    sleep(2)
    print "Right Clockwise"
    right_motor.clockwise()
    sleep(2)
    print "Right CC"
    right_motor.counter_clockwise()
    sleep(2)
    
except StandardError:
    print'Error running rover.py'
    
"""
def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()      
    except:
        print("Error writing to: " + property + " value: " + value)

       
try:
        set("delayed", "0")
        set("frequency", "500")
        set("active", "1")
        left_motor = Motor(left_in1_pin, left_in2_pin)
       
        direction = None
       
        while True:    
                cmd = raw_input("Command, f/r/o/p/s 0..9, E.g. f5 :")
               
                # if enter was pressed with no value, just stick with the current value
                if len(cmd) > 0:
                        direction = cmd[0]
                if direction == "f":
                        left_motor.clockwise()
                elif direction == "r":
                        left_motor.counter_clockwise()
                elif direction == "o": # opposite1
                        left_motor.counter_clockwise()
                elif direction == "p":
                        left_motor.clockwise()     
                else:
                        left_motor.stop()
               
                # only need to adjust speed if we want to      
                if len(cmd) > 1:
                        speed = int(cmd[1]) * 11
                        set("duty", str(speed))
               
except KeyboardInterrupt:
        left_motor.stop()
        print "\nstopped"
"""
