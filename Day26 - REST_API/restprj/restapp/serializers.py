from django.db import models
from django.db.models import fields
from rest_framework import serializers
from restapp.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields=('id','name','email','salary')
