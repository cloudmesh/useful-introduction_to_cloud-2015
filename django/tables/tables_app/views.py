from django.shortcuts import render
from django_tables2   import RequestConfig
from tables_app.models  import Person
from tables_app.tables  import PersonTable
from tables_app.tables import NameTable
# Create your views here.

def people(request):
	
	data = [
    		{"name": "Bradley", "ID": 1},
    		{"name": "Stevie", "ID" : 2},
	]	

	table = NameTable(data)
	RequestConfig(request).configure(table)
	return render(request, "tables_example.html", {'table': table})
