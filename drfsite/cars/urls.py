from django.urls import path
from .views import CarAPIView

urlpatterns = [
    path('car-list/', CarAPIView.as_view()),
    path('car-list/<int:pk>', CarAPIView.as_view()),
]