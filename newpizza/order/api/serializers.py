from rest_framework import serializers
from ..models import OrderItem, Order
from food.models import Food, Addition
from food.api.serializers import FoodSerializer, AdditionSerializer
from django.contrib.contenttypes.models import ContentType

class OrderedItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Food):
            serializer = FoodSerializer(value)
        elif isinstance(value, Addition):
            serializer = AdditionSerializer(value)
        else:
            raise Exception('Unexpected type of ordered item')
            
        return serializer.data

    def to_internal_value(self, data):
        return int(data)
            
class ContentTypeRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, value):
        model = ContentType.objects.get(app_label='food', model=value)
        return model

class OrderItemSerializer(serializers.Serializer):
    content_type = ContentTypeRelatedField(queryset=ContentType.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    item = OrderedItemRelatedField(queryset=OrderItem.objects.all())
    price = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        if validated_data.get('content_type').name == 'food':
            item = Food.objects.get(pk=validated_data.get('item'))
        elif validated_data.get('content_type').name == "addition":
            item = Addition.objects.get(pk=validated_data.get('item'))
        else:
            raise Exception('There is no such type of product')

        price = item.price * validated_data.get('quantity')

        instance = OrderItem(
            order = validated_data.get('order'),
            content_type = validated_data.get('content_type'),
            object_id = item.id,
            item= item,
            price = price,
            quantity = validated_data.get('quantity')
        )
        instance.save()

        return instance


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'first_name', 
            'last_name', 
            'address', 
            'postal_code', 
            'city', 
            'created', 
            'paid',
            'items',
            ]
   
    