# Generated by Django 5.0.6 on 2024-06-12 12:11

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
                ("description", models.TextField()),
                ("duration", models.IntegerField()),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
    ]
