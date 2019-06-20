from django.db import models


class TaskInfo(models.Model):
    name = models.TextField(primary_key=True, help_text="Name of the executed task")
    latest_execution_time = models.DateTimeField(null=True)


class BaseGeo(models.Model):
    start_date = models.DateField(null=True, help_text="The date a record first became relevant to a register.")
    end_date = models.DateField(null=True, help_text="The date a record stopped being applicable.")
    name = models.TextField(help_text="The commonly-used name of a record.")
    official_name = models.TextField(help_text="The official or technical name of a record.")

    class Meta:
        abstract = True


class Country(BaseGeo):
    country = models.TextField(
        primary_key=True,
        help_text="The country's 2-letter ISO 3166-2 alpha2 code.")
    citizen_names = models.TextField(help_text="The name of a country's citizens.")


class Territory(BaseGeo):
    territory = models.TextField(
        primary_key=True,
        help_text=("The territory's ISO 3166-1 alpha3 code."
                   "Unique codes have been created for territories that don't have an existing ISO code."))


class CountryTerritory(BaseGeo):
    country = models.TextField(
        null=True,
        help_text="The country's 2-letter ISO 3166-2 alpha2 code.")
    territory = models.TextField(
        null=True,
        help_text=("The territory's ISO 3166-1 alpha3 code."
                   "Unique codes have been created for territories that don't have an existing ISO code."))
    citizen_names = models.TextField(
        null=True,
        help_text="The name of a country's citizens.")
