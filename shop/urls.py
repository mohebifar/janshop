from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from rest_framework import serializers, viewsets, routers
from commerce.models import Product
from commerce.models import Category
from commerce.models import Structure

admin.autodiscover()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'images',)


class StructureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Structure
        fields = ('name',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    structures = StructureSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'structures')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^files-widget/', include('topnotchdev.files_widget.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
