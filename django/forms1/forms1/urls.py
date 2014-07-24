from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forms1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^post/form_upload.html$', 'app_forms.views.post_form_upload', name = 'post_form_upload'),
    url(r'^admin/', include(admin.site.urls)),
)
