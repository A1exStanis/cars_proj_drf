from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    content = serializers.CharField()
    power = serializers.CharField(max_length=20)
    max_speed = serializers.IntegerField(default=0)
    time_created = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
        