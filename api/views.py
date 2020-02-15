from rest_framework import viewsets, mixins, generics
from authentication.models import ChefProfile, CustomerProfile, Vote
from .serializers import ChefSerializer, CustomerSerializer, VoteSerializer, ItemSerializer, OrderSerializer
from ordering.models import Order, Item
from rest_framework.exceptions import ValidationError


class ChefViewSet(generics.RetrieveUpdateAPIView):
    queryset = ChefProfile.objects.none()
    serializer_class = ChefSerializer

    def get_queryset(self):
        return ChefProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        total_cost = 0
        items = serializer.data.get('items')
        for item in items:
            total_cost += item.price

        return serializer.save(customer=self.request.user, total_price=total_cost)


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
