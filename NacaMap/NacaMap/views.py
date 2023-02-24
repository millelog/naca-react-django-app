from django.shortcuts import render
import folium

def map_view(request):
    map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
    map = map._repr_html_() # render map as HTML
    return render(request, 'map.html', {'map': map})