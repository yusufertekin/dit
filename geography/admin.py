from django.contrib import admin

from geography.models import Country, Territory, CountryTerritory


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Territory)
class TerritoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CountryTerritory)
class CountryTerritoryAdmin(admin.ModelAdmin):
    pass
