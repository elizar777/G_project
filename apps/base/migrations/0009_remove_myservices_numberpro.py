# Generated by Django 5.0.3 on 2024-03-18 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_myservices_image_myservices_numberpro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myservices',
            name='numberpro',
        ),
    ]