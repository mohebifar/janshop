from django.conf.urls import patterns, include, url
from django.contrib import admin
from commerce.views import router

admin.autodiscover()

urlpatterns = patterns(

    '',
    url(r'^api/', include(router.urls)),
    url(r'^admin/files-widget/', include('topnotchdev.files_widget.urls')),
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', 'commerce.views.get_index', name='index'),

)

