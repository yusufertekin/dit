from geography.management.commands._private import GeoBaseCommand
from geography.models import Territory


class Command(GeoBaseCommand):
    help = "Import territories"
    model = Territory
    name = "territory"
    request_url = "https://territory.register.gov.uk/records.json"
