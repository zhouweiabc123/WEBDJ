#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#对项目进行操作的命令   http://127.0.0.1:8000/
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoPlateTest.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    #python manage.py runserver
    main()
