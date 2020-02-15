from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from management.models import Speciality

User = get_user_model()


PROFILE_STATUS = (
    ('PENDING', 'PENDING'),
    ('APPROVED', 'APPROVED')
)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name

    def email(self):
        return self.user.email


class ChefProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chef_profile')
    phone = models.CharField(max_length=15)
    percentage = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rating = models.FloatField(default=0.0)
    votes_count = models.IntegerField(default=0)
    status = models.CharField(choices=PROFILE_STATUS, default='PENDING', max_length=10)
    amount_due = models.FloatField(default=0)
    specialities = models.ManyToManyField(Speciality, blank=True)

    def __str__(self):
        return self.user.first_name

    def email(self):
        return self.user.email


class Vote(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=500, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voted')
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
