from setup import SteerMotor
from time import sleep
from rpisensors.proximity import VL6180X
from rpisensors.eeprom16 import Eeprom16

dist_sensor = VL6180X(1)
distance = 255

while distance >=  25:
    distance = dist_sensor.read_distance()
    print "Distance is" , distance, "mm"
    sleep(0.1)
    if distance < 25:
        print"You are too close to the car!"
