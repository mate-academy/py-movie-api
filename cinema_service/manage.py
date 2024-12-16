import os
import sys
from typing import NoReturn


def main() -> NoReturn:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_service.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
