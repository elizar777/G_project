# Generated by Django 5.0.3 on 2024-03-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_secondary'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondary',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]