from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import ChefProfile, CustomerProfile, Vote
from api.serializers import ChefSerializer, CustomerSerializer, VoteSerializer, ItemSerializer, OrderSerializer
from ordering.models import Order, Item


class ChefViewSet(viewsets.ModelViewSet):
    queryset = ChefProfile.objects.all()
    serializer_class = ChefSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer

class VoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



