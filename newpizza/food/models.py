from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.CharField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='ingredients/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Ingredients'
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ingredients = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='food/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Food'
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name
   


