# Generated by Django 5.0.2 on 2024-03-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
