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
]