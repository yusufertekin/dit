from django.views.generic.list import ListView

from geography.models import Country, Territory, CountryTerritory


class GeoBaseListView(ListView):
    title = None
    model = None
    template_name = None
    paginate_by = 50
    ordering = None
    header_order = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'field_map': self.get_field_map(),
            'title': self.title
        })
        return context

    def get_field_map(self):
        field_map = [(f.verbose_name.title(), f.name)
                     for f in self.model._meta.get_fields() if f.name in self.header_order]
        field_map = sorted(field_map, key=lambda x: self.header_order.index(x[1]))
        return field_map


class CountryListView(GeoBaseListView):
    title = "Countries"
    model = Country
    template_name = "geography/countries.html"
    ordering = "name"
    header_order = ['country', 'name', 'official_name', 'citizen_names', 'start_date', 'end_date']


class TerritoryListView(GeoBaseListView):
    title = "Territories"
    model = Territory
    template_name = "geography/territories.html"
    ordering = "name"
    header_order = ['territory', 'name', 'official_name', 'start_date', 'end_date']


class CountryTerritoryListView(GeoBaseListView):
    title = "Countries & Territories"
    model = CountryTerritory
    template_name = "geography/countries_and_territories.html"
    ordering = "name"
    header_order = ['country', 'territory', 'name', 'official_name', 'citizen_names', 'start_date', 'end_date']
