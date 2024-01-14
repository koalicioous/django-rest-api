"""
Django command to pause execution until database is available
"""
import time

from psycopg2 import OperationalError as PsyOperationalError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_ready = False
        while db_ready is False:
            try:
                self.check(databases=["default"])
                db_ready = True
            except (PsyOperationalError, OperationalError):
                self.stdout.write("Database unavailable, waiting 2 second...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available!"))
