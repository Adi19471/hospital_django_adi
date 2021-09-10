from django.shortcuts import render
from django.http import HttpResponse

from hospital .models import Hospitals
from patient .models import Patient


from django .db .models import Q

from django .db .models import Avg,Max,Min,Sum

# import forms contact form
from .forms import ContactForm,ContactModelForm

def index(request):
    return render(request,'base/index.html')


def all_model_quires(request):
    
    ALL = Patient.objects.filter(age__gt=10)
    query_display = ALL.query
    
    
    agr = Patient.objects.all().aggregate(Sum('age'),Min('age'),Max('age'),Avg('age'))
    
    counts = Patient.objects.all().count()
    
    
    
    # # firstnamelastname_dispaly = Patient.objects.filter(first_name__startswith="k") | Patient.objects.filter(last_name__endswith="m")
    # # last_first = firstnamelastname_dispaly.query
    
    # firstnamelastname_dispaly = Patient.objects.filter(Q(first_name__startswith="k") | Q(last_name__endswith="m"))
    
    
    # alldata = Patient.objects.exclude(first_name__istartswith='u')
    # show = alldata.query
    
    
    context = {
        'all': ALL,
        'query_display_key':query_display,
        
        'agr':agr,
        'counts':counts,
    
        
        # 'firstnamelastname_dispaly_key':firstnamelastname_dispaly,
        
        # 'alldata_key':alldata,
        # 'show_key':show,
        
        
        
    }
    return render(request, 'base/alldata.html',context)



def contact_view(request):
    if request.method == "POST": # POST always UPPERCASE 
        contact = ContactForm(request.POST)
        if contact.is_valid():
            return HttpResponse("Your data has submited")
            
    else:
        contact = ContactForm()
        
    return render(request, 'base/contact.html',{'contact':contact})

def ContactModelForm_view(request):
    if request.method == "POST":
        con = ContactModelForm(request.POST)
        if con.is_valid():
            # the form is saved in data in data base tabe
            
            con.save()
    else:
        con = ContactModelForm
            
    return render(request,'base/ContactModelFormdata.html',{'con':con})