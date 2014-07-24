from django.shortcuts import render
from models import Employee

# Create your views here.

def index(request):
        employee = Employee.objects.create(
		email="pedro.kong@company.com",
		first_name="Pedro",
		last_name="Kong"
    	)
    	employee.save()
    	return render(request, 'index.html', {})
