from django.db import models
from datetime import datetime, date
import os

# Create your models here.

class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    venue = models.CharField('Venue Name',max_length=120)
    event_date = models.CharField('Event Date',max_length=80,blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='img/')
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField('Full Name:',max_length=120)
    age = models.IntegerField('Age')
    email = models.EmailField('Email')
    phone = models.IntegerField('Phone Number')
    semester = models.IntegerField('Semester')
    college = models.CharField('College',max_length=120,default='')
    gender = models.CharField('Gender',max_length=20)
    event = models.CharField('Event Name',max_length=120,default='')

    def __str__(self):
        return self.name

