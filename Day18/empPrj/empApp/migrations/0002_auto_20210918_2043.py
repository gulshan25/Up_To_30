# Generated by Django 3.2.5 on 2021-09-18 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='Format: yyyy-mm-dd', verbose_name='Birth Date Fld '),
        ),
    ]
