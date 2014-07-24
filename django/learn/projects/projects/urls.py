from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ProjectInfos.views',
    # Examples:
    # url(r'^$', 'projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('ProjectInfos.urls')),
    url(r'^ProjectInfos/$', 'ProjectInfo_list'),
    url(r'^ProjectInfos/(?P<pk>[0-9]+)/$', 'ProjectInfo_detail'),
)
