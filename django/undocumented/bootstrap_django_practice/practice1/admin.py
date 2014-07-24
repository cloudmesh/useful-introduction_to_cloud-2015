from django.contrib import admin

# Register your models here.
from .models import Person

#class SignUpAdmin(admin.ModelAdmin):
	#class Meta:
		#model =SignUp
		
#admin.site.register(SignUp, SignUpAdmin)

class PersonAdmin(admin.ModelAdmin):
	class Meta:
		model =Person
		
admin.site.register(Person, PersonAdmin)


