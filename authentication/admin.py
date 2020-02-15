from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomerProfile, ChefProfile

User = get_user_model()

admin.site.unregister(User)


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__email',)
    list_display = ('__str__', 'email')


admin.site.register(CustomerProfile, ProfileAdmin)
admin.site.register(ChefProfile, ProfileAdmin)
