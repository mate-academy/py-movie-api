# Generated by Django 4.1 on 2022-10-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.PositiveIntegerField(),
        ),
    ]
