import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')
import django
django.setup()

from studentapp.models import student
from faker import Faker

fg=Faker()
def add_student():
    fname=fg.name()
    faddress=fg.address()
    femail=fg.email()
    fdob=fg.date()
    fgender='Male'
    fphone=fg.phone()
    fimage=fg.image()


    std=student.objects.get_or_create(fullname=fname, address=faddress, email=femail, dob=fdob, age=fage, gender=fgender, phone=fphone, image=fimage)[0]
    return std

def populate_data(n=10):
    for entry in range(n):
        std=add_student()

if __name__ == '__main__':
    print('#'*50)
    print('populating data Please wait...')
    populate_data()
    print('Data populated Complete')
    print('#'*50)             