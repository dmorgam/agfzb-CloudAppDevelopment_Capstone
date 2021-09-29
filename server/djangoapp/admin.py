from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarMake)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
        fields = ['model_id', 'name', 'dealer_id','car_type','year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
        fields = ['name', 'desc']
        inlines = [CarModelInline]

# Register models here
