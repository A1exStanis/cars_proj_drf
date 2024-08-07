from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Car, Class
from .serializers import CarSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']

        if not pk:
            return Car.objects.all()[:]

        return Car.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = Class.objects.all()
        return Response({'cats': [c.name for c in cats]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        cat = Class.objects.get(pk=pk)
        return Response({'cats': cat.name})

# class CarAPIList (generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#
# class CarAPIUpdate(generics.UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#
# class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
