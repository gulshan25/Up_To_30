from django.db import models
from datetime import datetime

# Create your models here.
class student(models.Model):
    GENDER_CHOICES=[('Male','Male'),('Female','Female'),]

    id=models.AutoField(primary_key=True)   
    fullname=models.CharField(max_length=100, blank=True)     
    address=models.CharField(max_length=128, blank=True)   
    email=models.EmailField(unique=True, blank=True)   
    dob=models.DateField(default=datetime.now, blank=True)   
    gender=models.CharField(max_length=8, choices=GENDER_CHOICES, default='Male')   
    age=models.CharField(max_length=3, blank=True)   
    phone=models.CharField(max_length=11, blank=True)  
    image = models.ImageField(upload_to='Static/img', height_field=None, width_field=None, max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{self.id} {self.fullname} {self.addr} {self.email} {self.dob} {self.gender} {self.age} {self.phone} {self.image}' 
