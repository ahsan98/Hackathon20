from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomerProfile, ChefProfile
from management.models import Shift

User = get_user_model()

# admin.site.unregister(User)


class ShiftInline(admin.StackedInline):
    model = Shift


class ChefAdmin(admin.ModelAdmin):
    search_fields = ('user__email',)
    list_display = ('__str__', 'email')
    inlines = [ShiftInline]


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('user__email',)
    list_display = ('__str__', 'email')


admin.site.register(CustomerProfile, CustomerAdmin)
admin.site.register(ChefProfile, ChefAdmin)
