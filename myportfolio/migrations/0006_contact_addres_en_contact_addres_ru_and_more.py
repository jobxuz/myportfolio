# Generated by Django 5.1.4 on 2025-01-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_remove_prayer_name_remove_prayer_time_prayer_asr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='addres_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='addres_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='addres_uz',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='city_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='city_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='city_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='date_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='date_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='date_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='desk_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='desk_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='desk_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
