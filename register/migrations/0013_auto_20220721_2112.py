# Generated by Django 3.2.14 on 2022-07-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20220721_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='recieverAddress',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='recieverFullName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='recieverPhoneNumber',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
