from django.conf.urls import patterns, include, url
from django.contrib import admin
from commerce.views import *
from commerce.api.product import *
from commerce.api.category import *
from commerce.api.brand import *

admin.autodiscover()

urlpatterns = patterns(

    '',
    url(r'^api/', include(router.urls)),
    url(r'^admin/files-widget/', include('topnotchdev.files_widget.urls')),
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/products/(?P<id>\d+)$', ProductDetail.as_view(), name='product-detail'),
    url(r'^api/products/', ProductSearchList.as_view(), name='product-search'),
    url(r'^$', 'commerce.views.get_index', name='index'),
    url(r'^/$', 'commerce.views.get_index', name='index'),
    url(r'^product', 'commerce.views.get_index', name='index'),

)

