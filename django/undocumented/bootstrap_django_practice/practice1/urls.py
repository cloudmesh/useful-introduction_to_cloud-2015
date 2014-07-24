from django.conf.urls import patterns, url

from practice1 import views

urlpatterns = patterns('',
	#url (r'^$', views.index, name='index'),
	url (r'^$', models.SignUp, name='=SignUp')
        url (r'^$', views.people, name = "people"),
)
