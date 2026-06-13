#!/usr/bin/env python
"""Command-line utility Django untuk tugas administratif."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog_sederhana.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Apakah Django sudah terinstall dan "
            "tersedia di environment PYTHONPATH? Apakah virtualenv sudah diaktifkan?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
