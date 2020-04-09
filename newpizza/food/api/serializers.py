from rest_framework import serializers
from ..models import Food, Ingredient, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class CategorySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializer(CategorySerializer):

    class Meta:
        model = Ingredient
        exclude = ('updated',)

    
class FoodSerializer(IngredientSerializer):

    class Meta:
        model = Food
        exclude = ('updated',)
            
        

    


    

