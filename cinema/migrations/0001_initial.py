# Generated by Django 5.0.4 on 2024-04-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(max_length=500)),
                ("duration", models.IntegerField()),
            ],
            options={
                "verbose_name": "movies",
            },
        ),
    ]
