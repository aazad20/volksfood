# Generated by Django 4.1.4 on 2024-01-05 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_alter_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='orderid',
        ),
    ]
