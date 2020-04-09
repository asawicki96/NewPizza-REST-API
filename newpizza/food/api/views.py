from rest_framework import viewsets
from .serializers import FoodSerializer, CategorySerializer, IngredientSerializer
from ..models import Food, Ingredient, Category
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminUser|ReadOnly]

class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAdminUser|ReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser|ReadOnly]
