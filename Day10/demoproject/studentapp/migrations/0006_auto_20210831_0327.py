# Generated by Django 3.2.6 on 2021-08-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20210831_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='middlename',
        ),
    ]
