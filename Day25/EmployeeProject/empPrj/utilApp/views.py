from django.contrib.messages.api import error
from empApp.models import *
from utilApp.forms import EmailForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
import csv
from empApp.models import Employee
from django.views.generic import *

from django.db.models import Count
from django.http import JsonResponse


# Create your views here.
def SendEmailwithAttachment(request):
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            email=form.cleaned_data['email']

            try:
                mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
                if request.FILES:
                    files=request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name,f.read(),f.content_type)

                mail.send()
                messages.success(request,'Email Send Successfully')
                return redirect('/')
            except Exception as ex1:

                print(ex1)
                messages.error(request,'email send hoi nai')

    else:
        form=EmailForm()

    context={'form':form}
    return render(request,'mail/mailform.html',context)

def export_employee_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="employee.csv"'
    writer=csv.writer(response)
    writer.writerow(['Id','Employee Name','Birth Date','Email-Address'])
    employees=Employee.objects.all().values_list('id','name','dob','email')
    for emp in employees:
        writer.writerow(emp)
    return response

class AboutView(TemplateView):
    template_name = "about.html" 
        
def group_by_dept(request): 
    querysets=Employee.objects.values('department__name').\
    annotate(num_employee=Count('department_id')).all()
    context={'querysets':querysets}
    return render(request,'utils/group_by_dept.html',context)

def show_chart(request,chartType):
    labels=[]
    data=[]
    charttype=chartType
    querysets=Employee.objects.values('department__name').annotate(num_employee=Count('department_id')).all()
    for qs in querysets:
        labels.append(qs['department__name'])
        data.append(qs['num_employee'])
    context={'labels':labels,'data':data,'charttype':charttype}
    return render(request,'utils/mychart.html',context)
    
