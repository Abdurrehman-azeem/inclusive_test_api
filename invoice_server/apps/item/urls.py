from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewset

router = DefaultRouter()
router.register('', ItemViewset, basename='item')

urlpatterns = [
    path('', include(router.urls))
]
