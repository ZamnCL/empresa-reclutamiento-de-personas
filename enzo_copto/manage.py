# Placeholder manage.py (you already have a real one in your project).
# Replace this with your existing manage.py if needed.
import os, sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enzo_copto.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
