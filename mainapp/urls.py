from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.registerPage,name='register'),
    path('loginpage',views.loginPage,name='loginpage'),
    path('faqs',views.faqs,name='faqs'),
    path('schedule',views.schedule,name='schedule'),
    path('speakers',views.speakers,name='speakers'),
    path('speakers_profile/<int:id>/',views.speakers_detail,name='speakers_profile'),
    path('sponsers',views.sponsers,name='sponsers'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('blog_detail/<int:id>/',views.blog_detail,name='blog_detail'),


]