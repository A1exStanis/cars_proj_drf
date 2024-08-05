from django.urls import path
from .views import CarAPIView, CarAPIList

urlpatterns = [
    path('car-list/', CarAPIList.as_view()),
    path('car-list/<int:pk>', CarAPIList.as_view()),
]