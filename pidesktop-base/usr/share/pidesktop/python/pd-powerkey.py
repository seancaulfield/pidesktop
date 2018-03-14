#!/user/bin/env python
#
# pd-powerkey.py - monitor GPIO to detect power key press
#

import RPi.GPIO as GPIO
import time,os,sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)  # Pi to Power MCU - start shutdown timer
GPIO.setup(33,GPIO.IN)   # Power MCU to Pi - power key pressed

GPIO.output(31,GPIO.LOW)  # tell PCU we are alive
GPIO.output(31,GPIO.HIGH) # cause blink by starting shutdown timer
time.sleep(0.5)
GPIO.output(31,GPIO.LOW)  # clear timer we really are alive

# callback function
def powerkey_pressed(channels):
    os.system("sync")
    os.system("shutdown -h now")
    sys.exit()

# wait for power key press
GPIO.add_event_detect(33,GPIO.RISING,callback=powerkey_pressed)

# idle - TODO: use wait
while True:
    time.sleep(10)
