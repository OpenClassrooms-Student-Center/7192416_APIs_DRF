from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryViewset, ProductView


router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/product/', ProductView.as_view()),
    path('api/', include(router.urls))
]
