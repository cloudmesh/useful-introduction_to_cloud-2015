html: clean
	cd doc; make html


clean:
	cd doc; make clean

view:
	cd doc/build/html; google-chrome index.html
