from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudmesh_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # admin pages
    url(r'^admin/', include(admin.site.urls)),


    # user pages
    url(r'^index/', 'cloudmesh_app.views.index', name = 'index'),
)
