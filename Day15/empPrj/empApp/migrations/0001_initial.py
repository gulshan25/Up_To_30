# Generated by Django 3.2.6 on 2021-09-12 21:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('dob', models.DateField(blank=True, default=django.utils.timezone.now, help_text='Format: yyyy-mm-dd', verbose_name='Birth Date')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monthly Salary')),
                ('photo', models.FileField(blank=True, default='myimage/blank.png', upload_to='myimage')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empApp.department')),
            ],
        ),
    ]
