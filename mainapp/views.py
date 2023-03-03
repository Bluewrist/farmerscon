from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from django.db.models import Q
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CustomUserCreationForm  
from.models import *


def home(request):
    blog = Blog_post.objects.all()[:3]
    if request.method == "POST":
        q = Questions()
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        question = request.POST.get('question')

        q.name = name
        q.email = email
        q.topic = topic
        q.question = question
        q.save()
        messages.success(request, 'Your question has been sent we will contact you as ppossible')
    context  = {
        'blog':blog
    }
    return render(request, "home.html",context)

def logoutPage(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return render(request,'home.html')

def loginPage(request):
    return render(request,'login.html')


def registerPage(request):
    if request.method == "POST":
        q = Registration()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        q.first_name = first_name
        q.last_name = last_name
        q.email = email
        q.phone = phone
        q.save()
        messages.success(request, 'Your have successfull registered for the farmerscon 2023')
    return render(request,'register.html')


def faqs(request):
    faq  = Faqs.objects.all()

    context  =  {
        'faq':faq,
    }

    return render(request,'faqs.html',context)

def schedule(request):

    return render(request,'schedule.html')


def speakers(request):
    speaker =  Speakers.objects.all()
    context =  {
        'speaker': speaker,
    }
    return render(request,'team.html',context)

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
    return render(request,'team.html',context)    


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Your message has been sent we will contact you as ppossible')
        
    return render(request, 'contact.html')



def blog(request):
    q =  request.GET.get('q') 
    if q == None:
        blog  = Blog_post.objects.all()
    else:
        blog = Blog_post.objects.filter(Q(category__name__icontains=q)|
                                Q(title__icontains=q)
                                )

    category =  Category.objects.all()
    recent = Blog_post.objects.all()[:5]
    page = request.GET.get('page')
    paginator = Paginator(blog, 2)
    try:
        blog = paginator.page(page)        
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog':blog,
        'category':category,
        'recent':recent,
    }
    return render(request,'blog.html',context)


def blog_detail(request,id):
    category =  Category.objects.all()
    blog = Blog_post.objects.get(id=id)
    context = {
        'blog':blog,
        'category':category
        
    }
    return render(request,'detail.html',context)
        