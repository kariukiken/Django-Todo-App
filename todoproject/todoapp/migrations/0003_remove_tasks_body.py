# Generated by Django 4.2.1 on 2023-05-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_tasks_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='body',
        ),
    ]
