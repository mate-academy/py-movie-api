# Generated by Django 4.2.2 on 2023-06-26 20:27

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
                ('title', models.CharField(max_length=63)),
                ('description', models.TextField(max_length=500)),
                ('duration', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
    ]
