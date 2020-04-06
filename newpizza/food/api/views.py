from rest_framework import viewsets
from .serializers import FoodListSerializer, CategoryDetailSerializer, IngredientListSerializer
from ..models import Food, Ingredient, Category


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer

class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
