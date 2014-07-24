from django.shortcuts import render
from django_tables2   import RequestConfig
from tables_app.models  import Person
from tables_app.tables  import PersonTable
from tables_app.tables import NameTable
from reservation.model import Reservation
import datetime
from mongoengine import *
from reservation.model import reservation_colabannect
# Create your views here.

def people(request):
	
	
	db = reservation_connect()

	reservation = Reservation(label="res-1",
                          	cm_id="reservation-res-1",
                          	summary="Simple reservation",
                          	host="i001",
                          	user="gregor",
                          	project="fg82",
                          	start_time=datetime.datetime(
                          		2014, 8, 1, 01, 00, 00),
                          	end_time=datetime.datetime(2014, 8, 1, 02, 00, 00))
        reservation.save()

	reservations = Reservation.objects(user="gregor")

	for reseravtion in reservations:
		data = [ 
			reservation


		#{"name": "Bradley", "ID": 1},
    		#{"name": "Stevie", "ID" : 2},
	]	

	table = NameTable(data)
	RequestConfig(request).configure(table)
	return render(request, "tables_example.html", {'table': table})
