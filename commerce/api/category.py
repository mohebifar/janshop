from rest_framework import serializers, viewsets
from rest_framework.response import Response
from commerce.models import Category
from structure import StructureSerializer
from brand import BrandSerializer
from commerce.views import router


class SubCategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'brands')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    structures = StructureSerializer(many=True, read_only=True)
    children = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'structures', 'children', 'image')


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        qs = Category.objects.all().filter(parent__isnull=True)

        serializer = CategorySerializer(qs, many=True)
        return Response(serializer.data)


router.register(r'categories', CategoryViewSet)