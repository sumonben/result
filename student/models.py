from typing import Iterable
from django.db import models

# Create your models here.
class Group(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

class Exam(models.Model):
    serial=models.IntegerField(default=0)
    title=models.CharField(max_length=150,blank=True,null=True)
    title_en=models.CharField(max_length=150,blank=True,null=True)
    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

class Student(models.Model):
    serial=models.IntegerField(default=0)
    roll=models.CharField(max_length=10,)
    name=models.CharField(max_length=150,blank=True,null=True)
    session=models.CharField(max_length=15,blank=True,null=True)
    category=models.CharField(max_length=50,blank=True,null=True)
    group=models.ManyToManyField(Group, blank=True,null=True)

  
class Subject(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,null=True,blank=True)
    name_en=models.CharField(max_length=100,unique=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    group=models.ManyToManyField(Group, blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name_en

class Marks(models.Model):
    serial=models.IntegerField(default=0)
    roll=models.CharField(max_length=10,)
    subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)
    exam=models.ForeignKey(Exam,blank=True,null=True,on_delete=models.SET_NULL)
    MCQ=models.IntegerField(blank=True,null=True)
    CQ=models.IntegerField(blank=True,null=True)
    practical=models.IntegerField(blank=True,null=True)
    total=models.IntegerField(blank=True,null=True)
    grade=models.CharField(max_length=150,blank=True,null=True)
    cpa=models.CharField(max_length=150,blank=True,null=True)
     
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.subject is not None:
            return self.roll+': '+self.subject.name_en
        return self.roll
    def subject_name(self):
        if self.subject is not None:
            return self.subject.name_en
    def save(self, *args, **kwargs):
        if self.CQ:
            if self.CQ<30:
                self.grade="F"
        super(Marks, self).save(*args, **kwargs)
