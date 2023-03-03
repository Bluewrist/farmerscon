from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Members(User):
    phone =  models.CharField(max_length=12)


    def __str__(self) :
        return self.first_name 

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self) :
        return self.first_name


    
    


class MemberProfile(models.Model):
    member = models.OneToOneField(Members,on_delete=models.CASCADE)

class Questions(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    topic =  models.CharField(max_length=100)
    question = models.TextField(max_length=1000)

    def __str__(self) :
        return self.name

class Faqs(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.question


class Speakers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  =  models.CharField(max_length=100)
    proffession  =  models.CharField(max_length=100)
    short_intro  =  models.CharField(max_length=100)
    bio  =  models.TextField(max_length=1000)
    profile_img = models.ImageField()

    def __str__(self) :
        return self.first_name


class Sponsers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self) :
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100) 
    email =  models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    
    
    def __str__(self) :
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=122)

class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="images")
    body = models.TextField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

