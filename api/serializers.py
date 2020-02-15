from rest_framework import serializers
from management.models import Kitchen, Shift, Speciality
from ordering.models import Item, Order
from authentication.models import CustomerProfile, ChefProfile, Vote
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CustomerProfile
        fields = ('user', 'phone',)


class ChefSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ChefProfile
        fields = ('user', 'phone', 'rating', 'votes_count', 'amount_due', 'status', 'specialities')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ('name', 'max_cooks')

class ShiftSerializer(serializers.Serializer):
    class Meta:
        model = Shift
        fields = '__all__'

class SpecialitySerializer(serializers.Serializer):
    class Meta:
        model = Speciality
        fields = ('name')

class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'