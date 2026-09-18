#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""

from __future__ import annotations

import os
import sys
from typing import NoReturn


def main() -> NoReturn:
    """Run Django administrative commands."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_api.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
