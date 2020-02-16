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
    user = UserSerializer(read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = ChefProfile
        fields = ('phone', 'rating', 'votes_count', 'amount_due', 'status', 'specialities', 'user', 'id')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('rating', 'comment', 'chef')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    chef = ChefSerializer(read_only=True)
    id = serializers.ReadOnlyField()
    menu_items_detailed = ItemSerializer(many=True, read_only=True)
    kitchen_name = serializers.StringRelatedField()

    class Meta:
        model = Shift
        fields = ('kitchen', 'start_time', 'end_time', 'status', 'menu_items', 'chef', 'id', 'menu_items_detailed', 'kitchen_name')


class KitchenSerializer(serializers.ModelSerializer):
    approved_shifts = ShiftSerializer(many=True)

    class Meta:
        model = Kitchen
        fields = ('name', 'id', 'approved_shifts')


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('name', 'id')


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    detailed_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('shift', 'chef', 'kitchen', 'items', 'status', 'id', 'detailed_items')
