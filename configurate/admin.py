from django.contrib import admin

from .models import ProductConfiguration

@admin.register(ProductConfiguration)
class ProductConfigurationAdmin(admin.ModelAdmin):
    list_display = ('complete_set', 'mat', 'shape', 'color', 'car_brand', 'car_model', 'production_year')
    search_fields = ('car_brand', 'car_model')  # Поиск по бренду и модели авто
    list_filter = ('complete_set', 'mat', 'shape', 'color', 'car_brand')  # Фильтрация по полям