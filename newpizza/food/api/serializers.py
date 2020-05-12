from rest_framework import serializers
from ..models import Food, Addition, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class CategorySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = Category
        fields = '__all__'


class AdditionSerializer(CategorySerializer):

    class Meta:
        model = Addition
        exclude = ('updated',)

    
class FoodSerializer(AdditionSerializer):

    class Meta:
        model = Food
        exclude = ('updated',)
            
        

    


    

