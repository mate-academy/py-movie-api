# Generated by Django 4.0.6 on 2022-07-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
