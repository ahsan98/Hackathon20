from django.urls import path, include
from rest_framework import routers
from .views import ChefViewSet, CustomerViewSet, VoteViewSet, OrderViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'vote', VoteViewSet)
router.register(r'item', ItemViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('chef/', ChefViewSet.as_view()),
    path('customer/', CustomerViewSet.as_view()),
    path('', include(router.urls))
]
