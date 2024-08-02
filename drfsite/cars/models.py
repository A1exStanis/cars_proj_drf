from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    power = models.CharField(max_length=20, null=True, blank=True)
    max_speed = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Class', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'


class Class(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
