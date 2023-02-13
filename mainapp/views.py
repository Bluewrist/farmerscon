from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm  
from.models import *


def home(request):
    return render(request, "home.html")

def logoutPage(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return render(request,'home.html')

def loginPage(request):
    
    return render(request,'login.html')


def registerPage(request):
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
        messages.success(request, 'Account created successfully')  
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request,'register.html',context)


def faqs(request):
    faq  = Faqs.objects.all()

    context  =  {
        'faq':faq,
    }

    return render(request,'faq.html',context)

def schedule(request):

    return render(request,'schedule.html')


def speakers(request):
    speaker =  Speakers.objects.all()
    context =  {
        'speaker': speaker,
    }
    return render(request,'profile.html',context)

def speakers_detail(request,id):
    speaker =  Speakers.objects.get(id=id)
    context =  {
        'speaker': speaker,
    }
    return render(request,'profile_detail.html',context)    


def sponsers(request):
    sponser =Sponsers.objects.all()
    context = {
        'sponser':sponser
    }
    return render(request,'sponsers.html',context)    


