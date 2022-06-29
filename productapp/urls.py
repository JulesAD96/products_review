from django.contrib import admin
from django.urls import path, include
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('products', ProductViewSet, basename='Product')
router.register('image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
]