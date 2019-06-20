from django.conf.urls import url, include

from geography.views import CountryListView, TerritoryListView, CountryTerritoryListView

urlpatterns = [
    url('^countries/', CountryListView.as_view(), name='countries'),
    url('^territories/', TerritoryListView.as_view(), name='territories'),
    url('^countries-territories/', CountryTerritoryListView.as_view(), name='countries-and-territories')
]
