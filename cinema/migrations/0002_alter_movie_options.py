# Generated by Django 5.0.6 on 2024-06-27 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"verbose_name": "movies"},
        ),
    ]
