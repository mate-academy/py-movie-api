# Generated by Django 5.0 on 2023-12-19 08:22

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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
                ("duration", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "movies",
            },
        ),
    ]
