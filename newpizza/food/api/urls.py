from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('food', views.FoodViewSet)
router.register('ingredients', views.IngredientsViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
