from django.contrib import admin

# Register your models here.
from .models import Hospital_Type,Hospitals


@admin.register(Hospitals)
class HospitalAdmin(admin.ModelAdmin):
    prepopulated_fields = {
         'slug': ['name'] 
    }

@admin.register(Hospital_Type)
class Hospital_TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['type_name']
    }
    

    
    