from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer


class CategoryView(APIView):

    def get(self, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
class ProductAPIView(APIView):
 
    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
