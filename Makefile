pidesktop: pidesktop-base.deb

pidesktop-base.deb:
	dpkg -b pidesktop-base/ pidesktop-base.deb

clean: pidesktop-base.deb
	rm -f pidesktop-base.deb

install: pidesktop-base.deb
	sudo dpkg -i pidesktop-base.deb

uninstall:
	sudo dpkg -r pidesktop-base

