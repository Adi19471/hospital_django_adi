from django.contrib import admin

# Register your models here.
from .models import Patient




class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    list_display_links = ['first_name','last_name']
    
    prepopulated_fields = {
        'slug':['first_name']
    }
    
  
admin.site.register(Patient,PatientAdmin)
