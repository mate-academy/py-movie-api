# Generated by Django 4.1.7 on 2023-04-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(null=True),
        ),
    ]
