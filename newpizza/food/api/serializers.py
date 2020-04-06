from rest_framework import serializers
from ..models import Food, Ingredient, Category

class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)

class CategoryDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializerField()
    
    class Meta:
        model = Category
        fields = (
            'id', 
            'name', 
            'slug', 
            'description', 
            'created', 
            'updated', 
            'tags'
        )


class IngredientListSerializer(CategoryDetailSerializer):
    price = serializers.SerializerMethodField('get_price')

    def get_price(self, obj):
        return str(obj.price)+" zł"

    class Meta:
        model = Ingredient
        fields = (
            'name',
            'slug',
            'price',
            'description',
            'image',
            'created',
            'tags'
        )

    
class FoodListSerializer(IngredientListSerializer):
    #ingredients = IngredientListSerializer(many=True, read_only=True)
    ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Food
        fields = (
            'id', 
            'name',
            'price', 
            'slug', 
            'ingredients', 
            'category', 
            'description',
            'image', 
            'created', 
            'tags'
        )