from django.urls import path, include

from rest_framework import routers
from .views import counters, auth


router = routers.SimpleRouter()
router.register('counters', counters.CounterViewSet, basename='counters')
urlpatterns = [
    path('auth/', auth.LoginApiView.as_view()),
    path('', include(router.urls)),
]

