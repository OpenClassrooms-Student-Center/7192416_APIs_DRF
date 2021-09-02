from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer


class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductViewset(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
