# Generated by Django 3.2.14 on 2022-07-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20220720_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='price',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='recieverAddress',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='recieverFullName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='courier',
            name='recieverPhoneNumber',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]