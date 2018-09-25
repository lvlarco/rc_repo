from time import sleep
from rpisensors.proximity import VL6180X
from rpisensors.eeprom16 import Eeprom16

dist_sensor = VL6180X(1)
distance = 255
dist_threshold = 25

while distance >=  dist_threshold:
    distance = dist_sensor.read_distance()
    print "Distance is" , distance, "mm"
    sleep(0.1)
    if distance < dist_threshold:
        print"You are too close to the car!"
