from django.db import models
from authentication.models import ChefProfile
from management.models import Kitchen

ORDER_STATUS = (
    ('PENDING', 'PENDING'),
    ('COOKING', 'COOKING'),
    ('COMPLETED', 'COMPLETED'),
    ('DECLINED', 'DECLINED')
)


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="items")

    def __str__(self):
        return self.name

class Order(models.Model):
    chef = models.OneToOneField(ChefProfile, on_delete=models.CASCADE, related_name="chefs_order")
    kitchen = models.OneToOneField(Kitchen, on_delete=models.CASCADE, related_name = "kitchens_order")
    items = models.ManyToManyField(Item)
    status = models.CharField(choices=ORDER_STATUS, default='PENDING', max_length=10)
    total_price = models.FloatField()

    def __str__(self):
        return self.chef.user.first_name + "-" + self.pk
