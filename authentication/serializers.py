from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import CustomerProfile, ChefProfile


class ExtendedRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    type = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['email'] = self.validated_data.get('email', '')
        data_dict['phone'] = self.validated_data.get('phone', '')
        data_dict['type'] = self.validated_data.get('type', '')

        return data_dict

    def save(self, request):
        user = super().save(request)
        user_type = self.cleaned_data.get('type')
        if user_type == 1:
            customer = CustomerProfile(phone=request.data['phone'], user=user)
            customer.save()
        elif user_type == 2:
            chef = ChefProfile(phone=request.data['phone'], user=user)
            chef.save()

        return user


class CustomUserSerializer(UserDetailsSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True, write_only=True)
    customer_profile = serializers.PrimaryKeyRelatedField(read_only=True)
    chef_profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone', 'chef_profile', 'customer_profile')
        model = get_user_model()

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['email'] = self.validated_data.get('email', '')
        data_dict['phone'] = self.validated_data.get('phone', '')

        return data_dict

    def save(self, **kwargs):
        pass
