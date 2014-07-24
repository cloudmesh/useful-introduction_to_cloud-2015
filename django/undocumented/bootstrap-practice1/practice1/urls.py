from django.conf.urls import patterns, url

from practice1 import views

urlpatterns = patterns('',
	url (r'^$', views.index, name='index')
)
