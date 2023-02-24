from django.shortcuts import render
import folium
from folium import Element

def update_map(request):
  # get the bounds parameter from the request
  bounds = request.GET.get("bounds")
  # do some logic based on the bounds, such as querying a database or an API
  # for example, you can get some points of interest within the bounds
  #pois = get_pois(bounds)
  print(bounds)
  # return some data as JSON that can be used by the JS code to update the map
  return ""

def map_view(request):
    map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    map = map._repr_html_() # render map as HTML
    return render(request, 'map.html', {'map': map})
