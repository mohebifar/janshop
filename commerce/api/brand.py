from rest_framework import serializers, viewsets
from commerce.models import Brand
from commerce.views import router
from rest_framework.response import Response


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        qs = Brand.objects.all()
        v = self.request.query_params.get('category')

        if v is not None:
            qs.filter(category__in=v)

        serializer = BrandSerializer(qs, many=True)
        return Response(serializer.data)


router.register(r'brands', BrandViewSet)