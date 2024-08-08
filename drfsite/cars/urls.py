from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'cars', CarViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('cars/', CarAPIList.as_view()),
    path('cars/<int:pk>', CarAPIUpdate.as_view()),
    path('carsdelete/<int:pk>', CarAPIDestroy.as_view())
]
