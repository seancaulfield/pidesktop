pidesktop: pidesktop-base.deb

pidesktop-base.deb:
	dpkg -b pidesktop-base/ pidesktop-base.deb

clean: pidesktop-base.deb
	rm -f pidesktop-base.deb

install: pidesktop-base.deb
	sudo dpkg -i pidesktop-base.deb

test:
	cp pidesktop-base/usr/share/pidesktop/script/pd-check       /usr/share/pidesktop/script
	cp pidesktop-base/usr/share/pidesktop/script/pd-clonessd    /usr/share/pidesktop/script
	cp pidesktop-base/usr/share/pidesktop/python/pd-bootssd.py  /usr/share/pidesktop/python
	cp pidesktop-base/usr/share/pidesktop/python/pd-fixrtc.py   /usr/share/pidesktop/python
	cp pidesktop-base/usr/share/pidesktop/python/pd-powerkey.py /usr/share/pidesktop/python
	cp pidesktop-base/usr/share/pidesktop/python/pd-shutdown.py /usr/share/pidesktop/python

uninstall:
	sudo dpkg -r pidesktop-base
