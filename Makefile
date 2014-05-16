html: clean
	mkdir -p doc/source/notebook
	cd notebook; ../bin/convert
	cd doc; make html


clean:
	cd doc; make clean

chrome:
	cd doc/build/html; google-chrome index.html

view:
	cd doc/build/html; open index.html
