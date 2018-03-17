Installation with mSATA SSD
===========================
It is VERY easy to build a new pidesktop case with a new mSATA SSD attached on a Raspberry Pi 3 Model B+ (2018) and only slightly more difficult for the older Model B.  If you have a choice, pick the Model B+, it can boot from SSD out of the box, has a faster CPU and networking. 

The pidesktop add-on board functions as a USB mSATA SSD device when connected to *any* system not just an RP3 Model B or B+. If the special USB adapter that connects the RP3 to the add-on card (hat) is not inserted and there is no SD card in the RP3, the RP3 will not boot. When the micro-USB data port of the add-on card is connected to a computer and power is provided via the second micro-USB port on the add-on card, the add-on card alone becomes a functional USB mSATA SSD device when the power button on the add-on card is pressed.

Needed parts:
- Pi Desktop Case
- Raspberry Pi 3 Model B+ (recommended) or Model B
- Formatted Blank SD card (recommended)
- mSATA SSD
- two USB->miniUSB cables (just for imaging)

Model B pre-install
-------------------
If you have a Model B+ you can skip this step, but if you have a Model B it may not have the ["Boot from USB bit"](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/msd.md) set by [booting from an SD card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) and making sure the required configuration bit is set in hardware. You should be able to use an existing SD card, just *remember* to clear the /boot/config.txt changes used the set the boot bit if you are going to reuse it. Make certain: `vcgencmd otp_dump | grep 17:` shows `17:3020000a`, then shutdown and replace the SD card with a formatted blank card to optimize boot times (which could be the same card).

Assemble the case
-----------------
Attach the RP3 board (with formatted blank SSD recommended) to the case using the provided posts. 
- Install the add-on board, and optionally a camera per the provided instruction booklet.
- Install the mSATA SSD onto the pidesktop add-on board and lock it in place with the provided small screws.
- DO NOT yet install the special USB adapter, first we need to image the SSD below.

Image your SSD
--------------
Use Etcher and the pidesktop add-on board (without the special USB adapter installed) as follows:
a. Connect both USB ports of the pi-desktop add-on board to two USB ports on the imaging machine
b. Press the power button on the add-on board, it will appear to your imaging system as a USB SSD device
c. Use Etcher to write the latest Raspian image (or your OS of choice) to the mSATA SSD USB device.
d. When complete unmount the USB SSD device and unplug the USB cables as they are no longer needed.

Test your Case
--------------
Now you can connect the special USB adapter to the case and boot with your monitor, keyboard, and mouse attached.  If you imaged Raspian the system shoud immediately reboot to resize partitions.  At this point, if you haven't already you can install the top on the case and know it takes a little pushing to get all the plastic clips in place.

Install the pidesktop package
-----------------------------
Good practice would be to [update Raspian via apt-get](https://www.raspberrypi.org/documentation/raspbian/updating.md) and then go to the [pidesktop github](http://github.com/hoopsurfer/pidesktop) to download the .deb package. Install the pidesktop-base package using the command `sudo dpkg -i pidesktop-base.deb` and reboot, check all is well with `pd-check` and you should see commands added, new services, and RTC clock updated.  You can then `shutdown now` and use the new pi-desktop power control - the blue led will flash for about 30 seconds and then full power off.

Best Feature: You can safely shutdown via the power button by holding it down for 2 seconds!

Test Installs with Different SSDs
---------------------------------
I was able to try different SSDs, I used Raspian images and the imaging process took about 8 minutes, once installed here are boot/reboot times measured first without an SD card installed, then with a blank SD card installed.  No cameras and the boot time was measured from pressing the power button to the first flash of the case LED - a feature of the [pidesktop 1.1.4 release](https://github.com/hoopsurfer/pidesktop).  The reboot time is from first flash of the case LED to case LED on - effectively when the reboot timer in the power MCU starts and ends.

__Raspberry Pi 3 Model B+ with Raspian Stretch 2018-03-13 - with and without a blank SD card__

 mSAT SSD Device  | *Boot Time to LED Flash* |  *Reboot Time w/o SD*  | *Reboot Time w/ Blank SD* 
------------------|--------------------------|------------------------|---------------------------
Samsung 860 EVO 250GB | 33.3 w/o SD, 27.9 w/SD | 30+s (reboot fails) | 27.7s-28.6s (fails sometimes)  
Kingston 120GB | 32.3s w/o SD, 27.2s w/SD | 30+s (reboot fails) | *26.4s-27.4s*
Kingspec 64GB | 32.3s w/o SD, 27.2s w/SD | 30+s (reboot fails) | 26.8s-29.9s (fails sometimes)

__Raspberry Pi 3 Model B (Boot from USB Set) with Raspian Stretch 2017-11-29 - with and without a blank SD card__

 mSAT SSD Device  | *Boot Time to LED Flash* |  *Reboot Time w/o SD*  | *Reboot Time w/ Blank SD* 
------------------|--------------------------|------------------------|---------------------------
Samsung 860 EVO 250GB | 32.7s w/o SD, 28.7 w/SD | 30+s (reboot fails) | 27.8s-28.6s (fails sometimes)  
Kingston 120GB | 31.2s w/o SD, 26.2s w/SD | 30+s (reboot fails) | *25.9s-26.8s*
Kingspec 64GB | 31.2s w/o SD, 26.2s w/SD | 30+s (reboot fails) | 26.3s-29.6s (fails sometimes)

A Few Observations:
- Note "Boot from USB" is enabled out of the box on the Model B+, however using a formatted blank SD card is still recommended.
- None of the devices was able to reboot consistently without a blank SD card inserted.
- The Kingston device has the fastest reboot times and so was less likely to fail to reboot.
- While boot times were fairly consistent, reboot times vary more that would be expected. 
As noted in the results reboots did fail and when they did it is bacause the boot process takes too long and the reboot timer elapses and shuts off power.  That timer is not always 30 seconds, in fact it seems more like 26s-27s when it does fail.  When reboot does fail it seems to be after previous reboots, not a reboot after a cold start.  I have reported what appears to be an underlying firmware bug.

Hacking Your Pi Desktop Case
----------------------------
If you ever need to reimage your mSATA SSD, it is as easy as unplugging the special USB adapter and connecting the micro-USB and and power ports to the imaging machine.  It takes me about 8 minutes to reimage and you *DO NOT* need to disassemble the case.   

If you use a wireless keyboard/mouse with your new pidesktop you can install the small dongle under the special USB adapter and that makes for a very clean installation with easy access to the remaining two USB ports.

If you're like me you want a clean look with no branding.  You can remove the branding in the center of the light ring by removing the plastic circle from the top of the case and then polishing off the branding using an abrasive like bar keepers friend liquid to remove the printing - lay the cloth on your bench and put a 2cm dot of abrasive liquid on a microfiber cloth to rub off the branding.

If you installed a camera you enable with "raspi-config" and then test it with `raspistill -vf -o test.jpg` and you can do some mild overclocking to speed up your new system - consider a micro cooling fan if you want to push your system.  

**FULL DISCLOSURE: Using a formatted blank SD card even though your system can boot from USB is strongly recommended. The pidesktop case power management firmware has a bug in that it expects reboot will always be completed in less than 30 seconds.  If your reboot times approach or exceed 30 seconds (and they can) you will experience failed or unreliable reboots which are effectively caused by the power management controller shutting off power because it cannot detect system restart during the early stages of a reboot.  The workaround is to insert a blank formatted SD card into your Raspberry Pi which will generally speed reboot times by around 5 seconds. If there is no SD card inserted, the SD boot mode takes about five seconds to fail before boot will start on the USB mSATA SSD.  Even if you don't have any reboot issues, you may want to save the 5 seconds and have a second storage device available for use.

References
----------
https://github.com/raspberrypi/documentation/blob/master/hardware/raspberrypi/bootmodes/bootflow.md
