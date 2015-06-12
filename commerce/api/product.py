from rest_framework import generics
from rest_framework import serializers, viewsets
from django.db.models import Q

from category import CategorySerializer
from detail import DetailSerializer

from commerce.views import router
from commerce.models import Product
from commerce.models import Detail


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
    related = serializers.ListField()

    class Meta:
        model = Product
        fields = ('name', 'image', 'long_name', 'price', 'images', 'category', 'details', 'description')

    def get_images(self, obj): return get_images(obj)


class ProductSearchList(generics.ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model
    paginate_by = 10

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        category = self.request.query_params.get('category', None)
        queryset = Product.objects.all()

        if query is not None:
            queryset = queryset.filter(Q(name__icontains=query) | Q(long_name__icontains=query))

        if category is not None:
            queryset = queryset.filter(category=category).order_by('?')[:4]

        return queryset


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()[:8]
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'


router.register(r'products', ProductViewSet)