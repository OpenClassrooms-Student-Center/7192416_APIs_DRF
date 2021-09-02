from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryView.as_view())
]
