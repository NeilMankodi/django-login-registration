# Generated by Django 3.0.5 on 2022-05-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
