# Generated by Django 5.1.7 on 2025-03-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='image',
        ),
        migrations.AddField(
            model_name='cargo',
            name='distance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cargo',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
