# Generated by Django 3.0.4 on 2020-03-09 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
    ]
