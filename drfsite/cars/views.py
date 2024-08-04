from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class CarAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

class CarAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        return Response({'posts': CarSerializer(cars, many=True).data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Car.objects.create(
            brand=request.data['brand'],
            model=request.data['model'],
            content=request.data['content'],
            power=request.data['power'],
            max_speed=request.data['max_speed'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': CarSerializer(post_new).data})
    