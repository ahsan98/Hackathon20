from django.urls import path, include
from rest_framework import routers
from .views import ChefViewSet, CustomerViewSet, VoteViewSet, OrderViewSet, ItemViewSet, SpecialityViewSet, \
    ShiftViewSet, KitchenViewSet, MarkComplete

router = routers.DefaultRouter()
router.register(r'vote', VoteViewSet)
router.register(r'item', ItemViewSet)
router.register(r'speciality', SpecialityViewSet)
router.register(r'shift', ShiftViewSet)
router.register(r'kitchen', KitchenViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('chef/', ChefViewSet.as_view()),
    path('customer/', CustomerViewSet.as_view()),
    path('order/complete/', MarkComplete.as_view()),
    path('order/', OrderViewSet.as_view()),
    path('', include(router.urls))
]
