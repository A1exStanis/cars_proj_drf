from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'max_speed', 'power', 'cat']
    list_editable = ['max_speed', 'power']
    search_fields = ['brand', 'model']
