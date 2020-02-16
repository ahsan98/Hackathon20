from django.db import models
# from ordering.models import Item

SHIFTS_STATUS = (
    ('PENDING', 'PENDING'),
    ('APPROVED', 'APPROVED')
)


class Speciality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    # TODO: location to be added

    def __str__(self):
        return self.name

    def approved_shifts(self):
        return self.shifts.filter(status='APPROVED') if hasattr(self, 'shifts') else Shift.objects.none()


class Shift(models.Model):
    chef = models.ForeignKey("authentication.ChefProfile", on_delete = models.CASCADE, related_name="shifts")
    kitchen = models.ForeignKey(Kitchen, on_delete = models.CASCADE, related_name="shifts")
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(choices=SHIFTS_STATUS, default='PENDING', max_length=10)
    menu_items = models.ManyToManyField("ordering.Item", blank=True)

    def menu_items_detailed(self):
        return self.menu_items

    def kitchen_name(self):
        return self.kitchen

# TODO: Checkin and checkout table

