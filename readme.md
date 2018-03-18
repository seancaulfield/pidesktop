pidesktop
===============
This repository is a fork of the "offical" DIY Pi Desktop Case supporting software sold by http://www.element14.com sourced from Embest Technology Ltd. The case comes with a novel mSATA USB Disk with a power management solution integrated with Raspberry Pi GPIO Connector.  Together they provide the missing mass storage and power management that is available in a typical desktop computer.  

The fork was created to apply patches requested by the community of users, to bring together all the related files and polish the product and support files since I would like to continue to use it, but with patches applied and cleaned up.  The approach here is focused on using a RP3 Model B+ (2018) and the USB mSATA SSD, if you don't take advantage of that capability there is not much point in purchasing the case.  It should work fine on an older RP3 Model B.

Install
-------
[Fast Installation booting from an mSATA drive](install.md)

[Standard Installation booting from an SD card](documents/Installation-Manual.md)

Utilities
----------
The original script utilities have been refactored and renamed

[pd-status](pidesktop-base/usr/share/pidesktop/script/pd-status) - summarize the files, scripts, links, and services to support pidesktop (new)

[pd-fixrtc.py](pidesktop-base/usr/share/pidesktop/python/pd-fixrtc.py) - install fixup to support RTC

[pd-clonessd](pidesktop-base/usr/share/pidesktop/script/pd-clonessd) - image SD to SSD and make bootable (was ppp-hdclone) 
which uses [pd-clonessd.py](pidesktop-base/usr/share/pidesktop/python/pd-clonessd.py) and [pd-bootssd.py](pidesktop-base/usr/share/pidesktop/python/pd-bootssd.py) 

systemd service files
---------------------
lib/systemd/system/pidesktop-shutdown.service which uses [pd-shutdown.py](pidesktop-base/usr/share/pidesktop/python/pd-shutdown.py)

lib/systemd/system/pidesktop-powerkey.service which uses [pd-powerkey.py](pidesktop-base/usr/share/pidesktop/python/pd-powerkey.py)

package files
-------------
control - package control info

postinst - post installation script

postrm = post uninstall script

building pidesktop-base
-----------------------
There is a simple Makefile to build pidesktop-base.deb file from sources or you can simply download the provided .deb file and install with the following command:

dpkg -i pidesktop-base.deb

If you want to change things you can clone this repository `make uninstall`, make your changes to the underlying code, then `make install` to build a new .deb package and install it.
