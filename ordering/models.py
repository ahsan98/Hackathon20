from django.db import models
from authentication.models import ChefProfile, CustomerProfile
from management.models import Kitchen

ORDER_STATUS = (
    ('PENDING', 'PENDING'),
    ('COOKING', 'COOKING'),
    ('COMPLETED', 'COMPLETED'),
    ('DECLINED', 'DECLINED')
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to="items", null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
    chef = models.ForeignKey(ChefProfile, on_delete=models.CASCADE, related_name="orders")
    shift = models.ForeignKey('management.Shift', on_delete=models.CASCADE, related_name="orders")
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(Item, blank=True)
    status = models.CharField(choices=ORDER_STATUS, default='PENDING', max_length=10)
    total_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chef.user.first_name + "-" + str(self.pk)
