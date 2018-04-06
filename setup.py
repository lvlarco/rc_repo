import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class DriverMotor(object):

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
 
    def __init__(self, steer_right_pin, steer_left_pin, steer_pin):
        self.steer_right_pin = steer_right_pin
        self.steer_left_pin = steer_left_pin
        self.steer_pin = steer_pin
         
        GPIO.setup(self.steer_right_pin, GPIO.OUT)
        GPIO.setup(self.steer_left_pin, GPIO.OUT)
        GPIO.setup(self.steer_pin, GPIO.OUT)
         
    def steer_right(self):
        GPIO.output(self.steer_right_pin, True)
        GPIO.output(self.steer_left_pint, False)
        GPIO.output(self.steer_pin, True)
         
    def steer_left(self):
        GPIO.output(self.steer_right_pin, False)
        GPIO.output(self.steer_left_pint, True)
        GPIO.output(self.steer_pin, True)
         
    def steer_stop(self):
        GPIO.output(self.steer_right_pin, False)
        GPIO.output(self.steer_left_pint, False)
        GPIO.output(self.steer_pin, False)

GPIO.cleanup()

"""
#try:

left_motor = Motor(left_in1_pin, left_in2_pin, driver_pin)
right_motor = Motor(right_in1_pin, right_in2_pin, driver_pin)

print "Left Clockwise"
left_motor.clockwise()
sleep(2)
print "Left CC"
left_motor.counter_clockwise()
sleep(2)
left_motor.stop()
print "Right Clockwise"
right_motor.clockwise()
sleep(2)
print "Right CC"
right_motor.counter_clockwise()
sleep(2)
right_motor.stop()
    
#except StandardError:
#    print'Error running rover.py'
     
GPIO.cleanup()
    

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
