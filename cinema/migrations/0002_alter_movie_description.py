from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="description",
            field=models.CharField(max_length=255),
        ),
    ]
