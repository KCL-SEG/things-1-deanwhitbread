from django.core.management.base import BaseCommand, CommandError
from things.models import Thing

class Command(BaseCommand):
    def handle(self, *args, **options):
        all_entries = Thing.objects.all()
        all_entries.delete()
