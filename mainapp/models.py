from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Members(User):
    pass


class MemberProfile(models.Model):
    pass   


class Faqs(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=1000)

    def __str__(self) :
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
    

