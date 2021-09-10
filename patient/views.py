from django.shortcuts import render

# Create your views here.

# model import patient 
from .models import Patient


def Patient_view(request):
    all_patient = Patient.objects.all()
    
    context = {
        'all_patient':all_patient
    }
    return render(request, 'patient/patient.html',context)


def Patient_detailes(request,nameslug):
    all_diplay = Patient.objects.filter(slug = nameslug)
    context = {
        'all_display_detailes':all_diplay
    }
    
    return render(request, 'patient/patient_detailes.html',context)