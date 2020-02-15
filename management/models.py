from django.db import models



SHIFTS_STATUS = (
    ('PENDING', 'PENDING'),
    ('APPROVED', 'APPROVED')
)

# Create your models here.


class Speciality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    # TODO: location to be added

    def __str__(self):
        return self.name


class Shift(models.Model):
    chef = models.ForeignKey("authentication.ChefProfile", on_delete = models.CASCADE, related_name="shifts")
    kitchen = models.ForeignKey(Kitchen, on_delete = models.CASCADE, related_name="shifts")
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(choices=SHIFTS_STATUS, default='PENDING', max_length=10)

# TODO: Checkin and checkout table

