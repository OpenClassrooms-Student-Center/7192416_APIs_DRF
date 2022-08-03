from rest_framework.serializers import ModelSerializer

from shop.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','date_created','date_updated','name','category']
        
