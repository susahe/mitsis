from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=128, unique=True)
    discription = models.CharField(max_length=128)
  
    
    def __unicode__(self):
        return (self.name)
    
class Module(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=128, unique=True)
    discription = models.CharField(max_length=128)
  
    
    def __unicode__(self):
        return (self.name)

class Topic(models.Model):
    module = models.ForeignKey(Module)
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=128, unique=True)
    discription = models.CharField(max_length=128)
  
    
    def __unicode__(self):
        return (self.name)

class Lesson(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=128, unique=True)
    discription = models.CharField(max_length=128)
  
    
    def __unicode__(self):
        return (self.name)
    
class Activity(models.Model):
    lesson = models.ForeignKey(Lesson)
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=128, unique=True)
    discription = models.CharField(max_length=128)
  
    
    def __unicode__(self):
        return (self.name)