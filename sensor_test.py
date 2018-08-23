from setup import SteerMotor
from time import sleep
from rpisensors.proximity import VL6180X
from rpisensors.eeprom16 import Eeprom16

# Default address
VL6180X_I2CADDRESS = 0x29

VL_IDENTIFICATION_MODEL_ID = 0x000
VL_SYSTEM_INTERRUPT_CONFIG_GPIO = 0x014
VL_SYSTEM_INTERRUPT_CLEAR = 0x015
VL_SYSTEM_FRESH_OUT_OF_RESET = 0x016
VL_SYSTEM_MODE_GPIO1 = 0x011
VL_SYSRANGE_START = 0x018
VL_SYSRANGE_INTERMEASUREMENT_PERIOD = 0x01B
VL_SYSRANGE_VHV_RECALIBRATE = 0x02E
VL_SYSRANGE_VHV_REPEAT_RATE = 0x031
VL_SYSALS_START = 0x038
VL_SYSALS_INTERMEASUREMENT_PERIOD = 0x03E
VL_SYSALS_ANALOGUE_GAIN = 0x03F
VL_SYSALS_INTEGRATION_PERIOD = 0x040
VL_RESULT_INTERRUPT_STATUS_GPIO = 0x04F
VL_RESULT_ALS_VAL = 0x050
VL_RESULT_RANGE_VAL = 0x062
VL_READOUT_AVERAGING_SAMPLE_PERIOD = 0x10A

VL_IDENTIFICATION_MODEL_ID_VALUE = 0xB4

VL_ALS_GAIN_1 = 0x06
VL_ALS_GAIN_1_25 = 0x05
VL_ALS_GAIN_1_67 = 0x04
VL_ALS_GAIN_2_5 = 0x03
VL_ALS_GAIN_5 = 0x02
VL_ALS_GAIN_10 = 0x01
VL_ALS_GAIN_20 = 0x00
VL_ALS_GAIN_40 = 0x07

#bus_id = VL6180X
#eeprom = Eeprom16(bus_id, VL6180X_I2CADDRESS)
dist_sensor = VL6180X(1)

distance = 0

while distance < 10:
    print distance
    
    dist_log = dist_sensor.read_distance()
    print dist_log
    status = Eeprom16().read_byte(VL_RESULT_INTERRUPT_STATUS_GPIO)
    range_status = status & 0x07
    
 #   if range_status == 0x04:
    value = Eeprom16().read_byte(VL_RESULT_RANGE_VAL)
      #  break

    sleep(1)

    Eeprom16().write_byte(VL_SYSTEM_INTERRUPT_CLEAR, 0x07)

    print "Distance is %(value) mm"
    distance = distance + 1
