# Generated by Django 4.1.7 on 2023-03-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230316_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='description',
        ),
        migrations.AddField(
            model_name='data',
            name='capital_city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
