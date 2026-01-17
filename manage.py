#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Same here: use underscore package name
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_security.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
