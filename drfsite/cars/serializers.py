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

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.content = validated_data.get('content', instance.content)
        instance.power = validated_data.get('power', instance.power)
        instance.max_speed = validated_data.get('max_speed', instance.max_speed)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance
