#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render #, render_to_response, RequestContext
#from django_tables2   import RequestConfig
#from practice1.models  import Person
#import django_tables2 as tables
#from practice1.tables  import PersonTable
#from django.http import HttpResponse
#import datetime


#def current_datetime(request):
	#now = datetime.datetime.now()
	#t = get_template('practicetemplate.html')
	#html = t.render(Context({'current_date':now}))
	#return HttpResponse(html)


























# Create your views here.

#def index(request):

	#html = """<!DOCTYPE html>

#<html>
	#<head>
	#</head>
	
	#<body>
		#<table style="width:300px">
		#<tr>
			#<td> Jeff</td>
			#<td> Ridgeway</td>
			#<td> 19 </td>
		#</tr>
		#<tr>
			#<td> Marian </td>
			#<td> Ridgeway </td>
			#<td> 50 </td>
		#</tr>
		#</table>
	#</body>
#</html>"""
	#result = str(index.html) 

	#return HttpResponse(html)

#def example1(request):



#data = [
    #{"name": "Bradley"},
   # {"name": "Stevie"},
    #{"last_name": "Richardson"},
    #{"last_name": "Bradley"},
#]

#class NameTable(tables.Table):
    #name = tables.Column()
    #class Meta:
        	#model = Person
        # add class="paleblue" to <table> tag
        	#attrs = {"class": "paleblue"}
   
#table = NameTable(data)



def people(request):
	#table = PersonTable(Person.objects.all())
    	#RequestConfig(request).configure(table)
   	#return render(request, 'people.html', {'table': table})
	return render(request, "people.html", {"people": Person.objects.all()})

	



