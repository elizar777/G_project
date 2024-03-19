# Generated by Django 5.0.3 on 2024-03-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_secondary_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_job', models.CharField(max_length=255, verbose_name='Тип работы')),
                ('skills', models.CharField(max_length=255, verbose_name='Каким образом пользователь делает работу')),
                ('numberservice', models.IntegerField(verbose_name='Номер сервисы (порядок)')),
            ],
            options={
                'verbose_name': 'Услуги пользователя',
                'verbose_name_plural': 'Услуги пользователей',
            },
        ),
        migrations.AlterField(
            model_name='infouser',
            name='skills',
            field=models.CharField(max_length=255, verbose_name='Каким образом пользователь делает работу'),
        ),
    ]
