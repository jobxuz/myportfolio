# Generated by Django 5.1.4 on 2025-01-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0006_contact_addres_en_contact_addres_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='current_temp2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='day_temp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='evening_temp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='morning_temp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
