from django import forms
from django.db.models import fields    
from studentapp.models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        # fields=('fullname','email','dob','gender','phone','address','age')
        fields='__all__'


