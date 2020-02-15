from django.contrib import admin
from .models import Speciality, Kitchen, Shift

# Register your models here.
class ShiftInline(admin.StackedInline):
    model = Shift

class KitchenAdmin(admin.ModelAdmin):
    inlines = [ShiftInline]

admin.site.register(Speciality)
admin.site.register(Kitchen, KitchenAdmin)