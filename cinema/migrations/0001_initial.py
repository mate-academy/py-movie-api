# Generated by Django 4.2 on 2023-04-05 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
