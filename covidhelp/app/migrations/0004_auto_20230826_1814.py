# Generated by Django 3.2.17 on 2023-08-26 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230826_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availbilities', to='app.facility')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availbilities', to='app.hospital')),
            ],
        ),
    ]
