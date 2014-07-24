PWD=`pwd`
PROJECT=`basename \`pwd\``

all:
	echo $(PROJECT)

create:
	django-admin.py startproject $(PROJECT)

start:
	python manage.py syncdb

stop:
	killall python

view:
	python manage.py runserver
	open http://127.0.0.1:8000/admin

clean:
	rm -f *.sqlite3
	rm -f *.pyc */*.pyc */*/.pyc
static:
	python manage.py collectstatic
