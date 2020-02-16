from rest_framework import viewsets, mixins, generics
from authentication.models import ChefProfile, CustomerProfile, Vote, Speciality
from .serializers import ChefSerializer, CustomerSerializer, VoteSerializer, ItemSerializer, OrderSerializer, \
    SpecialitySerializer, ShiftSerializer, KitchenSerializer
from ordering.models import Order, Item
from rest_framework.exceptions import ValidationError
from management.models import Shift, Kitchen


class ChefViewSet(generics.RetrieveUpdateAPIView):
    queryset = ChefProfile.objects.none()
    serializer_class = ChefSerializer

    def get_queryset(self):
        return ChefProfile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)

    def get_object(self):
        qs = self.get_queryset()
        obj = qs[0] if len(qs) else None
        return obj


class CustomerViewSet(generics.RetrieveUpdateAPIView):
    queryset = CustomerProfile.objects.none()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return CustomerProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_object(self):
        qs = self.get_queryset()
        obj = qs[0] if len(qs) else None
        return obj


class KitchenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer


class VoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        vote = Vote.objects.filter(customer=self.request.user, chef_id=serializer.validated_data.get('chef'))
        if vote:
            raise ValidationError({'chef': 'You have already reviewed this chef'})
        created_vote = serializer.save(customer=self.request.user)
        chef = created_vote.chef.chef_profile
        chef.votes_count = Vote.objects.all().count()
        chef.rating = 0
        votes = Vote.objects.filter(chef=chef.user)
        for vote in votes:
            chef.rating += vote.rating
        chef.rating /= chef.votes_count
        chef.save()

        return created_vote


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.none()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'customer_profile'):
            return self.request.user.customer_profile.orders
        elif hasattr(self.request.user, 'chef_profile'):
            return self.request.user.chef_profile.orders

    def perform_create(self, serializer):
        total_cost = 0
        items = serializer.data.get('items')
        for item in items:
            total_cost += item.price

        order = serializer.save(customer=self.request.user, total_price=total_cost)
        chef = order.chef
        admin_percentage = (100.0 - chef.percentage)/100
        chef.amount_due += total_cost * admin_percentage
        chef.save()
        return order


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SpecialityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ShiftViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Shift.objects.none()
    serializer_class = ShiftSerializer

    def get_queryset(self):
        return Shift.objects.filter(chef=self.request.user.chef_profile)

    def perform_create(self, serializer):
        return serializer.save(chef=self.request.user.chef_profile)
