from django.db import models
from food.models import Food, Addition
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Order(models.Model):
    first_name = models.CharField('Imię', max_length=50)
    last_name = models.CharField('Nazwisko', max_length=50)
    email = models.EmailField('E-mail')
    address = models.CharField('Adres', max_length=250)
    postal_code = models.CharField('Kod pocztowy', max_length=20)
    city = models.CharField('Miejscowość', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, 
        limit_choices_to={'model__in':('food', 'addition')},
        on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity    