from django.core.management import BaseCommand
from servise.jobs import test_job

class Command(BaseCommand):
    def handle(self, *args, **options):
        test_job()
