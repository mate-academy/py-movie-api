# Generated by Django 4.2.7 on 2023-11-28 21:14

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
                ("title", models.CharField(max_length=55)),
                ("description", models.TextField(blank=True, default="")),
                ("duration", models.IntegerField()),
            ],
        ),
    ]
