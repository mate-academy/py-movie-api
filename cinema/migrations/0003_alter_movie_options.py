# Generated by Django 4.2.3 on 2023-07-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_alter_movie_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'movies'},
        ),
    ]
