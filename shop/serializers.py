from rest_framework.serializers import ModelSerializer

from shop.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
