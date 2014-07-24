from django.conf.urls import patterns, url

from practice2 import views

urlpatterns = patterns('',
	url (r'^$', views.display, name='display')
)
