from django.shortcuts import render,redirect

from .models import User
from .forms import SignupForm,LoginForm

from django.contrib.auth import authenticate,login ,logout as log
from django.contrib import messages
# Create your views here.
def userlogin(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = SignupForm()
    return render(request, 'user/userlogin.html',{'fm':fm})

def login_view(request):
    if request.method =="POST":
        form = LoginForm()
        uname = request.POST.get("username")
        upass = request.POST.get("password")
        
        print("usr name",uname)
        print("password name",upass)
        
        user_data = authenticate(username=uname,password=upass)
        #user_data = authenticate(uname=username,upass=password)
        
        if user_data is not None:
            login(request, user_data)
            return redirect('/')
        else:
            messages.error(request,"your data doesnot match our record")
    
    else:
        form = LoginForm()
    return render(request,'user/loginpage.html',{'user':form})


def logout_view(request):
    
    log(request)
    
    messages.info(request, "Logged out successfully!")
    return redirect('/')
    
    
