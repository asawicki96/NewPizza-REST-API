from rest_framework import viewsets
from .serializers import FoodSerializer, CategorySerializer, AdditionSerializer
from ..models import Food, Addition, Category
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.response import Response
from ..documents import FoodDocument, AdditionDocument

''' Permission class allowing only safe methods requests '''

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


''' CRUD viewset for Food model '''

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def get_queryset(self):
        tag = self.request.GET.get('tag', None).split(',')
        searchfield = self.request.GET.get('searchfield', None)
        if searchfield:  
            queryset = FoodDocument.search().filter('multi_match', query=searchfield,
                        fields=['name', 'slug', 'description', 'ingredients']).to_queryset()
        elif tag:
            queryset = Food.objects.filter(tags__name__in=tag).distinct()
        else:
            queryset = Food.objects.all()
        return queryset


''' CRUD viewset for Addition model '''

class AdditionViewSet(viewsets.ModelViewSet):
    queryset = Addition.objects.all()
    serializer_class = AdditionSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    
    def get_queryset(self):
        searchfield = self.request.GET.get('searchfield', None)
        if searchfield:  
            queryset = AdditionDocument.search().filter('multi_match', query=searchfield,
                        fields=['name', 'slug', 'description', 'tags']).to_queryset()
        elif tag:
            queryset = Addition.objects.filter(tags__name__in=tag).distinct()
        else:
            queryset = Addition.objects.all()
        return queryset

''' CRUD viewset for Category model '''

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser|ReadOnly]
