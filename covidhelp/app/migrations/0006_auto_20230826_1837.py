# Generated by Django 3.2.17 on 2023-08-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230826_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
