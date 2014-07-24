from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_practice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    
    url(r'^practice1/', include ('practice1.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/', 'practice1.views.index' , name = 'index'),
    #url(r'^currenttime/', 'practice1.views.current_datetime' , name = 'currenttime'),
    #url(r'^practice2/', 'practice2.views.display', name = 'display'),
)
