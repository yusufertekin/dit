from django.core.management.base import BaseCommand

from geography.models import Country


class Command(BaseCommand):
    help = "Import countries"

    def handle(self, *args, **options):
        for obj in Country.objects.all():
            print(obj.name)
