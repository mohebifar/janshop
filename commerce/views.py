from django.shortcuts import render_to_response

from rest_framework import serializers, viewsets, routers
from commerce.models import Product
from commerce.models import Category
from commerce.models import Structure


def get_index(request):
    return render_to_response('front/index.html')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'images', 'image', 'long_name', 'price', )


class StructureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Structure
        fields = ('name',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    structures = StructureSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'structures')


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('-id')[:10]
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)