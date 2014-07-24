from django.shortcuts import render
from django_tables2   import RequestConfig
from tables_django_app.models  import Person
from tables_django_app.tables  import PersonTable
from tables_django_app.tables import NameTable
#from django.db import models
#from .models import Person
# Create your views here.

#def index(request):
	#return render(request, 'tables_django_example.html',)

def people(request):

	data = [
    		{"name": "Bradley", "ID": 1},
    		{"name": "Stevie", "ID" : 2},
	]	

	table = NameTable(data)
	#table = PersonTable(Person.objects.all())
	RequestConfig(request).configure(table)

	return render(request, "tables_django_example.html", {'table': table})
	#return render(request, "tables_django_example.html",)


