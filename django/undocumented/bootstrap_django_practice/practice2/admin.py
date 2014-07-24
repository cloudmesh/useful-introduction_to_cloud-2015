from django.contrib import admin

# Register your models here.
from .models import Book

'''class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model =SignUp
		
admin.site.register(SignUp, SignUpAdmin)'''

class BookAdmin(admin.ModelAdmin):
	class Meta:
		model = Book

admin.site.register(Book, BookAdmin)

