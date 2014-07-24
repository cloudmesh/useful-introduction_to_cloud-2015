from django.conf.urls import patterns, include, url

from django.contrib import admin
from InfoProjects import views
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projects2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('InfoProjects.urls')),
    url(r'^InfoProjects/$', views.InfoProject_list.as_view()),
    url(r'^InfoProjects/(?P<pk>[0-9]+)/$', 'InfoProject_detail'),	
    #url(r'^index/', 'InfoProjects.views.index', name = 'index'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
