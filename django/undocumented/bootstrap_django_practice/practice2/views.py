from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.db import models


def display(request):
	return render(request, 'practice2/template/template.html', {'obj': models.Book.objects.all()})




'''def display(request):
	return render_to_response('template.tmpl', {'obj': models.Book.objects.all()})'''
	













'''from mongoengine import *
from reservation.model import reservation_connect
from reservation.model import Reservation
from reservation.plot import timeline_plot


# Create your views here.

def index(request):

	connect('reservation', port = 27777)

	reservations = Reservation.objects()
	result = "<table>"
	for reservation in reservations:
        	result = result + "<tr>" 

		for attribute in reservation:
			result = result + "<td>"
			result = result + reservation[attribute]
			result = result + "</td>"

		result = result + "</tr>" + "\n"


	print 70*"D"
	print result
	print 70*"D"

	result = "</table>"
	return HttpResponse(result)'''











