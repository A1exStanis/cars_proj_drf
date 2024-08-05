from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CarAPIList (generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        return Response({'posts': CarSerializer(cars, many=True).data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'put': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        instance.delete()
        return Response({'delete': 'Object has been deleted'})