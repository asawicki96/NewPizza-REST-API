from django.contrib import admin
from .models import Food, Category, Addition

# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'tag_list', 'created']
    list_filter = ['created', 'tags']
    search_fields = ['name', 'category__name']
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    def amount(self, obj):
        return str(obj.price)+" zł"

@admin.register(Category)
class CategoryAdmin(FoodAdmin):
    list_display = ['name', 'tag_list', 'created']
    
@admin.register(Addition)
class IngredientAdmin(FoodAdmin):
    pass


