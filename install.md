Installation with mSATA SSD
===========================
It is very easy to build a new pidesktop case with a new mSATA SSD attached. The official documents make this unecessarily complex with creating SD cards and clone operations. If you want the fast path here it is!

Needed parts:
- Pi Desktop Case
- Raspberry Pi 3 (RP3)
- mSATA SSD
- a bootable SD card (just for installing)
- two USB->miniUSB cables (just for imaging)

The pidesktop add-on board functions as a USB mSATA SSD device when connected to *any* system not just an RP3. If the special USB adapter that connects the RP3 to the add-on card (hat) is not installed and there is no SD card in the RP3, the RP3 will not boot. When the micro-USB data port of the add-on card is connected to a computer and power is provide via the second micro-USB port the add-on card is funcational when the power button is pressed.

Before you assemble the case
----------------------------
Make sure the RP3's ["Boot from USB bit"](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md) is set by [booting from an SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) and making sure the required bit is set in hardware.  Make certain: *vcgencmd otp_dump | grep 17:* shows *17:3020000a*, then shutdown and remove the SD card since it is no longer needed.  You should be able to use an existing card, just *remember* to clear the /boot/config.txt changes used the set the boot bit.

Assemble the case
-----------------
Install the RP3 board (no SD required), the add-on board and optionally a camera per the provided instruction booklet.
Install the mSATA SSD onto the pidesktop add-on board with the provided small screws.
DO NOT yet install the special USB adapter, first we need to image the SSD.

Image your SSD
--------------
Using Etcher and the pidesktop add-on board (without the special USB adapter) with the following steps:
a. Attach both USB ports of the pi-desktop add-on board with USB cables to the imaging machine
b. Press the power button on the add-on board, it will appear to your imaging system as a USB SSD device
c. Use Etcher to write the latest Raspian image (or you OS of choice) to the mSATA SSD USB device.
d. When complete unmount the USB SSD device and unplug the USB cables they are no longer needed.

Test your Case
--------------
Now you can connect the special USB adapter to the case and boot with your monitor, keyboard, and mouse attached.  If you imaged Raspian the system shoud immediately reboot to resize partitions.  At this point, if you haven't already you can install the top on the case.

Install the pidesktop package
-----------------------------
Good practice would be to [update Raspian via apt-get](https://www.raspberrypi.org/documentation/raspbian/updating.md) and go to the pidesktop github to download the zipped .deb package. Unzip then install the pidesktop-base package and reboot, check all is well with *sudo hwclock -r* and *shutdown now* will use the new pi-desktop power control - blue led will flash then full power off.

If you installed a camera you enable with "raspi-config" and then test it with *raspistill -vf -o test.jpg* and you can do some mild overclocking can speed up your new system - add a fan (case supports it) if you want to push your system.  Best Feature: You can safely shutdown via the power button by holding it down for 2 seconds!

Remember
--------
If you ever need to reimage your mSATA SSD, it is as easy as unplugging the special USB adapter and connecting the micro-USB and and power ports to the imaging machine.  You *DO NOT* need to disassemble the case.   Also, if you use a wireless keyboard/mouse with your new pidesktop you can install the small dongle under the special USB adapter and that makes for a very clean installation with easy access to the remaining USB ports.
