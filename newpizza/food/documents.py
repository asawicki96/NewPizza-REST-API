from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Food, Addition, Category
from taggit.managers import TaggableManager

@registry.register_document
class FoodDocument(Document):
    category = fields.ObjectField(properties = {'name': fields.TextField()})
    tags = fields.ObjectField(properties = {'name': fields.TextField()})

    class Index:
        name = 'food'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Food
        fields = [
            'name',
            'slug',
            'price',
            'ingredients',
            'description',
            'image',
            'size',
            'created',  
        ]
        related_models = [Category]

        
@registry.register_document
class AdditionDocument(Document):
    class Index:
        name = 'additions'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Addition
        fields = [
            'name',
            'slug',
            'price',
            'description',
            'image',
            'size',
            'created'
        ]

