Installation with Berryboot and an mSATA SSD
============================================
This is the EASIEST approach to setting up a pi-desktop case and while it does require a dedicated SD card it can also be the FASTEST if you have a good network connection and for some it is even faster than manually imaging your mSATA SSD.

This approach is easiest because it eliminates any SD card changes that might be needed and the SD card you install inside the case is intended to stay there.   Berryboot which is a light weight boot manager placed on your Pi's SD card which then allows you to boot one or more OSs from your SSD.  The approach described here requires downloading an OS from the network, while there are other approaches they are not covered here.    

Needed parts:
- Pi Desktop Case
- Raspberry Pi 3 Model B+ (recommended) or Model B
- Formatted Blank SD card (4GB or larger)
- mSATA SSD

SD Preparation
-------------------
Download the latest [Berryboot .zip](https://www.berryterminal.com/doku.php/berryboot) file to a system that can write to your SD card, format the card with a utility like the [Official SD Formatter](https://www.sdcard.org/downloads/index.html) and extract all the files in the .zip file into your SD card.  If you look at the SD card you should see all the files at the top level or root of the SD card (not all in a sub-directory).  Quickly boot your Pi with the card (connected to a monitor, keyboard and mouse).  You should see the Bootberry Menu and you can do the initial configuration (more on this below) or just turn off your Pi and configure it after the case is assembled.

Assemble the case
-----------------
Attach the RP3 board (with just prepped SD card) to the case using the provided offset posts
- Install optionally connect a camera per the provided instruction booklet
- Install the add-on board connecting the 40-pin connector and secure with the provided top posts 
- Install the mSATA SSD onto the pidesktop add-on board and lock it in place with the provided small screws
- Install the special USB adapter to connect together the add-on board to your Pi's USB port
At this point you can install the top on the case and know it takes a little pushing to get all the plastic clips in place.

Test your Case
--------------
Make sure the special USB adapter is firmly in place, your monitor, keyboard, and mouse attached and power on your case with the power button.  The blue "halo" should light and your Pi should boot, configure Berryboot overscan, network, audio, timezone, keyboard appropriate for you. Click OK, select your mSATA SSD, click Format and you are ready to install an OS.

As of this writing you can choose the official Raspian distribution, but you can also choose other options like OpenELEC, Ubuntu Mate, or RetroPie.  For these instructions we'll assume you choose Raspian Stretch which when testing these instructions took 4 minutes to download and install.  Press OK to reboot and when the menu come up click Edit Menu (you have 10 seconds).

Before you boot Raspian for the first time, it is recommended to shorten the wait time of Berryboot so reboots work well.  Click Edit Config, select the cmdline.txt tab and edit the boot menu timeout value.  If you are quick with your mouse 1 second works, if you're not sure try 3 seconds.   You can set your new image to boot by default, click on Exit to reboot into Raspian.

You may never need to touch Berryboot again, it will boot into your new Raspian image every time as is.  If you want to install other OS images you can learn more about [Berryboot](https://berryterminal.com/doku.php/berryboot) and try it.

Install the pidesktop package
-----------------------------
Good practice at this point would be to [update Raspian via apt](https://www.raspberrypi.org/documentation/raspbian/updating.md) and then with your browser hit [pidesktop github](http://github.com/hoopsurfer/pidesktop) to download the .deb package. Install the pidesktop-base package using the command `sudo dpkg -i pidesktop-base.deb` and reboot, check all is well with `pd-check` and you should see commands added, new services, and RTC clock updated.  You can then `shutdown now` and use the new pi-desktop power control - the blue led will flash for about 30 seconds and then full power off.

Best Feature: You can safely and quickly shutdown via the power button by holding it down for 2 seconds!
