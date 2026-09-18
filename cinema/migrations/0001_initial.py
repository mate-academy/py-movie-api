"""Initial database migration for the cinema app."""

from __future__ import annotations

from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    """Create the Movie database table."""

    initial = True
    dependencies: list[tuple[str, str]] = []
    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("duration", models.PositiveIntegerField(validators=[MinValueValidator(1)])),
            ],
            options={"ordering": ["id"]},
        ),
    ]
