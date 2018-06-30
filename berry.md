Installation with Berryboot and an mSATA SSD
============================================
This is the EASIEST approach to setting up a pi-desktop case and while it does require a dedicated SD card it can also be the FASTEST if you have a good network connection and for some it is even faster than manually imaging your mSATA SSD.

Key features of pidesktop:

- Reliable reboot with mSATA SSD drives
- Flash on boot to signal pidesktop support is enabled
- Improved installation instructions (Raspian and Bootberry)
- New pd-check command that provides detailed environment support
- Improved logging information
- Improved systemd services
- Rationalized file naming scheme

This approach is easiest because it eliminates any SD card changes that might be needed and the SD card you install inside the case is intended to stay there.   Berryboot which is a light weight boot manager placed on your Pi's SD card which then allows you to boot one or more OSs from your SSD.  The approach described here requires downloading OS images from the network, while there are other approaches they are not covered here.    

Needed parts:
- Pi Desktop Case
- Raspberry Pi 3 Model B+ (recommended) or Model B
- Formatted Blank SD card (4GB or larger)
- mSATA SSD

SD Preparation
-------------------
Download the latest [Berryboot .zip](https://www.berryterminal.com/doku.php/berryboot) file to a system that can write to your SD card, format the card with a utility like the [Official SD Formatter](https://www.sdcard.org/downloads/index.html) and extract all the files in the .zip file into your SD card.  If you look at the SD card you should see all the files at the top level or root of the SD card (not all in a sub-directory).  Quickly boot your Pi with the card (and connected to a monitor, keyboard and mouse).  You should see the Bootberry Menu (more on this below). Turn off your Pi and configure it after the case is assembled.

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

Before you boot Raspian for the first time, it is recommended to shorten the wait time of Berryboot so reboots work well.  Click Edit Config, select the cmdline.txt tab and edit the boot menu timeout value to 3-5 seconds.  You can set your new image to boot by default, click on Exit to reboot into Raspian.

You may never need to touch Berryboot again, it will boot into your new Raspian image every time as is.  If you want to install other OS images you can learn more about [Berryboot](https://berryterminal.com/doku.php/berryboot) and try it.

Install the pidesktop package
-----------------------------
Good practice would be to [update Raspian via apt-get](https://www.raspberrypi.org/documentation/raspbian/updating.md) and while those instructions work, using a higher-level `apt` with the following commands is growing in popularity:
- `sudo apt update`
- `sudo apt full-upgrade`

Now you can go to the [pidesktop github](http://github.com/hoopsurfer/pidesktop) to download the .deb package from your browser. Install the pidesktop-base package using the command `sudo dpkg -i pidesktop-base.deb` and reboot, check all is well with `pd-check` and you should see your firmware & kernel versions, new commands added, new services, and RTC clock updated, and finally a summary of the installed pidesktop package.

**NOTE: CHECK THAT FIRMWARE IN `pd-check` IS DATED 2018-06-29 OR NEWER! A needed firmware update that we requested has been made that dramatically improves reboot reliability.  You can wait for the patch to make it into a formal release or if you do want to use the pre-release firmware you can run `rpi-update` to install the newest firmware build. Shutdown and restart and recheck that you have newer firmware with the `pd-check` command again.

Now you can then hit the case power button for 2 seconds and your Pi should immediately shutdown.  You can issue `shutdown now` or `reboot` (or the equivalent) and the case led will flash until reboot has started (~10 secs) or longer for shutdown (~30 secs) get to full power off.

