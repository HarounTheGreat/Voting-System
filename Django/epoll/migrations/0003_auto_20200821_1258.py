# Generated by Django 2.0.7 on 2020-08-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epoll', '0002_auto_20200821_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='Candidate Picture'),
        ),
    ]
