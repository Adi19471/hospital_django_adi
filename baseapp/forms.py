from django import forms

from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(label="Enter your name",label_suffix=':-',max_length="100")
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    
    

class ContactModelForm(forms.ModelForm):
    name = forms.CharField(label="Enter Your Name",min_length=10 ,required=True ,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Enter Your Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label="Enter Your Mobile Number",widget=forms.TextInput(attrs={'class':'form-control'}))
    messages = forms.CharField(label="Enter Your Messages",widget=forms.TextInput(attrs={'class':'form-control'}))
   
    
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
        
    
