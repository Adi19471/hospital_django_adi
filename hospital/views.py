from django.shortcuts import render

# here is only importing moel data
from .models import Hospitals

# Create your views here.

# here only founction based classes 

def hospital_data_view(request):
    
    # i am importing the model data only here all data display hopital 
    Hospital_all_data = Hospitals.objects.all()  # query set select * from . Hospital
    return render(request,'hospital/hospital.html',{'Hospital_all_data':Hospital_all_data})