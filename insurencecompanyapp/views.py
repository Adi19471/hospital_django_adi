from django.shortcuts import render


from .models import Company
# Create your views here.
def get_insurence_detailes(request):
    company_detailes = Company.objects.all()
    
    context={
        'company_detailes':company_detailes
    }
    
    return render(request, 'patient_company/insurence.html',context)
    