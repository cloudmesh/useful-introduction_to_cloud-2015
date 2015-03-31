PATHNAME=$(shell pwd)
BASENAME=$(shell basename $(PATHNAME))

TAG=`echo "print __version__" > v.py;  cat cloudmesh/__init__.py v.py > /tmp/v1.py; python /tmp/v1.py; rm /tmp/v1.py v.py`

all: banner
	fab doc.all

pdf:
	fab doc.pdf

epub:
	fab doc.epub


slides: banner
	fab doc.slides

fast: banner
	fab doc.fast

view:
	fab doc.view

banner:
	@echo
	@echo "======================================================================"
	@echo


######################################################################
# INSTALLATION
######################################################################
req:
	pip install -r requirements.txt

dist:
	make -f Makefile pip

sdist: clean
	#make -f Makefile clean
	python setup.py sdist --format=bztar,zip


force:
	make -f Makefile nova
	make -f Makefile pip
	pip install -U dist/*.tar.gz

install:
	pip install dist/*.tar.gz

######################################################################
# PYPI
######################################################################

upload:
	make -f Makefile pip
#	python setup.py register
	python setup.py sdist upload

pip-register:
	python setup.py register

######################################################################
# QC
######################################################################

qc-install:
	pip install pep8
	pip install pylint
	pip install pyflakes

qc:
	pep8 ./cloudmesh/virtual/cluster/
	pylint ./cloudmesh/virtual/cluster/ | less
	pyflakes ./cloudmesh/virtual/cluster/

# #####################################################################
# CLEAN
# #####################################################################


clean:
	rm -rf *.egg
	find . -name "*~" -exec rm {} \;  
	find . -name "*.pyc" -exec rm {} \;  
	rm -rf build dist *.egg-info *~ #*
	rm -rf *.egg-info
	rm -rf *.log *.pid
	rm -rf docs/build

uninstall:
	yes | pip uninstall cloudmesh


#############################################################################
# PUBLISH GIT HUB PAGES
###############################################################################

publish:
	fab doc.publish


######################################################################
# TAGGING
######################################################################

print_tag:
	@echo "VERSION: $(TAG)"

tag:
	@echo "VERSION: $(TAG)"
	make clean
	python bin/util/next_tag.py
	git tag $(TAG)
	echo $(TAG) > VERSION.txt
	git add .
	git commit -m "adding version $(TAG)"
	git push



