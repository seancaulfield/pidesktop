#!/user/bin/env python

# pd-shutdown.py - oneshot service so do your thing and exit
#
# We are in shutdown processing either because shutdown or reboot is running or because
# the power button was pressed.  If we're here because the power button was pressed then 
# Power MCU is already in Waiting OFF state and will turn off immediately if it sees 
# pin 31 go high.  If power button has not been pressed we should inform power MCU 
# shutdown/reboot is taking place so the shutdown timer can start.
#
# Note: The timer will reset when the Pi powers off so the only purpose REALLY for doing
# this is to force a power off if shutdown hangs for some reason - somewhat lame.

import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use physical board pin numbering
GPIO.setup(31,GPIO.OUT)  # Pi to Power MCU communication
GPIO.setup(33,GPIO.IN)   # Power MCU to Pi on power button press

# stash the current system clock setting into the RTC hardware
os.system("/sbin/hwclock --systohc")

if GPIO.input(33):
	# Power Key was already pressed - shut the system down immediately
else:
	# shutdown or reboot not related to power key
	GPIO.output(31,GPIO.HIGH) #  tell power MCU and exit immediately
