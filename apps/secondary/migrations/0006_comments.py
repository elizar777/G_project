# Generated by Django 5.0.3 on 2024-03-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_alter_tags_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('data', models.DateField(verbose_name='Когда был отзыв')),
                ('description', models.CharField(max_length=255, verbose_name='Отзыв оставляете здесь')),
                ('image', models.ImageField(upload_to='comments/', verbose_name='Фото клиента')),
            ],
            options={
                'verbose_name': 'Отзывы клиента',
                'verbose_name_plural': 'Отзывы клиентов',
            },
        ),
    ]