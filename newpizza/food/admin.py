from django.contrib import admin
from .models import Food, Category, Ingredient

# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'tags', 'created']
    list_filter = ['created', 'tags']
    search_field = ['name', 'tags']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tags', 'created']
    list_filter = ['created', 'tags']
    search_field = ['name', 'tags']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'tags', 'created']
    list_filter = ['created', 'tags']
    search_field = ['name', 'tags']

