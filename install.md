Installation with mSATA SSD
===========================
It is very easy to build a new pidesktop case with a new mSATA SSD attached. The official documents make this unecessarily complex with creating SD cards and clone operations. If you want the fast path here it is!

Needed parts:
- Pi Desktop Case
- Raspberry Pi 3 (RP3)
- mSATA SSD
- a bootable SD card (just for installing)
- two USB->miniUSB cables (just for imaging)

The pidesktop add-on board functions as a USB mSATA SSD device when connected to *any* system not just an RP3. If the special USB adapter that connects the RP3 to the add-on card (hat) is not inserted and there is no SD card in the RP3, the RP3 will not boot. When the micro-USB data port of the add-on card is connected to a computer and power is provided via the second micro-USB port on the add-on card, the add-on card alone becomes a functional USB mSATA SSD device when the power button on the add-on card is pressed.

Before you assemble the case
----------------------------
Make sure the RP3's ["Boot from USB bit"](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md) is set by [booting from an SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) and making sure the required bit is set in hardware.  Make certain: `vcgencmd otp_dump | grep 17:` shows `17:3020000a`, then shutdown and remove the SD card since it is no longer needed**.  You should be able to use an existing card, just *remember* to clear the /boot/config.txt changes used the set the boot bit.

**FULL DISCLOSURE:  The pidesktop case power management firmware has a bug in that it expects reboot will always be completed in less than 30 seconds.  If your reboot times approach or exceed 30 seconds (and they can) you will experience failed or unreliable reboots which are effectively caused by the power management controller shutting off power because it cannot detect system restart during the early stages of a reboot.  The workaround is to insert a blank formatted SD card into your Raspberry Pi which will generally speed reboot times by around 5 seconds. If there is no SD card inserted, the SD boot mode takes five seconds to fail before boot will start on the USB mSATA SSD.  Even if you don't have any reboot issues, you may want to save the 5 seconds and have a second storage device available for use.

Assemble the case
-----------------
Install the RP3 board (no SD required), the add-on board and optionally a camera per the provided instruction booklet.
Install the mSATA SSD onto the pidesktop add-on board with the provided small screws.
DO NOT yet install the special USB adapter, first we need to image the SSD.

Image your SSD
--------------
Using Etcher and the pidesktop add-on board (without the special USB adapter installed) with the following steps:
a. Attach both USB ports of the pi-desktop add-on board with USB cables to the imaging machine
b. Press the power button on the add-on board, it will appear to your imaging system as a USB SSD device
c. Use Etcher to write the latest Raspian image (or you OS of choice) to the mSATA SSD USB device.
d. When complete unmount the USB SSD device and unplug the USB cables they are no longer needed.

Test your Case
--------------
Now you can connect the special USB adapter to the case and boot with your monitor, keyboard, and mouse attached.  If you imaged Raspian the system shoud immediately reboot to resize partitions.  At this point, if you haven't already you can install the top on the case.

Install the pidesktop package
-----------------------------
Not required when I tested, but good practice would be to [update Raspian via apt-get](https://www.raspberrypi.org/documentation/raspbian/updating.md) and then go to the [pidesktop github](http://github.com/hoopsurfer/pidesktop) to download the .deb package. Install the pidesktop-base package and reboot, check all is well with `pd-check` and you should see commands added, new services, and RTC clock updated. You can then `shutdown now` and use the new pi-desktop power control - blue led will flash for 30 seconds and then full power off.

If you installed a camera you enable with "raspi-config" and then test it with `raspistill -vf -o test.jpg` and you can do some mild overclocking to speed up your new system - add a micro cooling fan (case supports it) if you want to push your system.  Best Feature: You can safely shutdown via the power button by holding it down for 2 seconds!

Test Installs with Different SSDs
---------------------------------
I was able to try different SSDs, generally the imaging process took about 4 minutes, once installed here are boot/reboot times measured first without an SD card installed, then with a blank SD card installed.  No cameras and the boot time was measured from pressing the power button to the first flash of the case LED (feature of this pidesktop 1.1.4 release).  The reboot time is from first flash of the case LED to case LED on - intended to start when the reboot timer starts).

__Raspberry Pi 3 Model B (Boot from USB Set) - with and without a blank SD card__

 mSAT SSD Device  | *Boot Time to LED Flash* |  *Reboot Time w/o SD*  | *Reboot Time w/ Blank SD* 
------------------|--------------------------|------------------------|---------------------------
Samsung 860 EVO 250GB | testing ongoing | ? | ?
Kingston 120GB | 31.2s w/o SD, 26.2s w/SD | 30+s (reboot fails) | 25.9s-26.8s
Kingspec 64GB | 31.2s w/o SD, 26.2s w/SD | 30+s (reboot fails) | 26.3s-29.6s (occastional fails)

__Raspberry Pi Model B+ with and without a blank SD card__

TODO:  Pi 3 Model B SD (not Boot from USB)

Remember
--------
If you ever need to reimage your mSATA SSD, it is as easy as unplugging the special USB adapter and connecting the micro-USB and and power ports to the imaging machine.  You *DO NOT* need to disassemble the case.   Also, if you use a wireless keyboard/mouse with your new pidesktop you can install the small dongle under the special USB adapter and that makes for a very clean installation with easy access to the remaining USB ports.

References
----------
https://github.com/raspberrypi/documentation/blob/master/hardware/raspberrypi/bootmodes/bootflow.md

