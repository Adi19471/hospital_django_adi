from django.shortcuts import render


from .models import Claim

# Create your views here.
def get_claims_data(request):
    insurencedata = Claim.objects.all()
    
    context = {
        'insurencedata':insurencedata
    }
    
    return render(request, 'claims/claim_data.html',context)
