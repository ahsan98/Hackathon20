from django.urls import path, include
from rest_framework import routers
from authentication.views import ChefViewSet, CustomerViewSet, VoteViewSet, OrderViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'chef', ChefViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'vote', VoteViewSet)
router.register(r'item', ItemViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls))
]
