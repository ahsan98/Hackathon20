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

    class Meta:
        model = CustomerProfile
        fields = ('phone',)


class ChefSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField()
    votes_count = serializers.ReadOnlyField()
    amount_due = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = ChefProfile
        fields = ('phone', 'rating', 'votes_count', 'amount_due', 'status', 'specialities')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('rating', 'comment', 'chef')


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ('name', 'max_cooks')


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class SpecialitySerializer(serializers.Serializer):
    class Meta:
        model = Speciality
        fields = ('name', )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('chef', 'kitchen', 'items', 'status')
