# Generated by Django 3.2.14 on 2022-07-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20220720_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(max_length=4),
        ),
    ]
