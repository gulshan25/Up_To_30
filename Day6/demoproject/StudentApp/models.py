from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES=[('Male', 'Male'),('Female', 'Female'), ('Other', 'Other'),]

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, blank=True)
    dob=models.DateField(default=datetime.now, blank=True)
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.gender}'