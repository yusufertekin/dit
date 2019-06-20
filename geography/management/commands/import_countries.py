from geography.management.commands._private import GeoBaseCommand
from geography.models import Country


class Command(GeoBaseCommand):
    help = "Import countries"
    model = Country
    name = "country"
    request_url = "https://country.register.gov.uk/records.json"
