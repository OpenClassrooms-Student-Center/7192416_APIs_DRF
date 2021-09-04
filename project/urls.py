from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from shop.views import CategoryViewset, ProductViewset, ArticleViewset,\
    AdminCategoryViewset, AdminArticleViewset


router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/article', AdminArticleViewset, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]
