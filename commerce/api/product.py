from rest_framework import generics
from rest_framework import serializers, viewsets
from django.db.models import Q

from category import CategorySerializer
from detail import DetailSerializer
from commerce.models import Product


def images_prefix(image): return '/static/media/' + image


def get_images(obj):
    return map(images_prefix, obj.images.split('\n'))


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'long_name', 'price', 'category')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = CategorySerializer()
    details = DetailSerializer(many=True, read_only=True)

    def get_images(self, obj): return get_images(obj)

    class Meta:
        model = Product
        fields = ('name', 'image', 'long_name', 'price', 'images', 'category', 'details', 'description', 'available')


class ProductSearchList(generics.ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model
    paginate_by = 16

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        category = self.request.query_params.get('category', None)
        random = self.request.query_params.get('random', None)
        price = self.request.data.get('price', None)
        brand = self.request.data.get('brand', None)
        queryset = Product.objects.all()

        if query is not None:
            queryset = queryset.filter(Q(name__icontains=query) | Q(long_name__icontains=query))

        if category is not None:
            queryset = queryset.filter(category=category)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        if price is not None:
            queryset = queryset.filter(price__lte=price)

        if random is not None:
            queryset = queryset.order_by('?')[:4]

        return queryset


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()[:8]
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'