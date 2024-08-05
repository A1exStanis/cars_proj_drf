from django.urls import path
from .views import *

urlpatterns = [
    path('car-list/', CarAPIList.as_view()),
    path('car-list/<int:pk>', CarAPIUpdate.as_view()),
    path('car-detail/<int:pk>', CarAPIDetailView.as_view()),
]