from django.shortcuts import render
from NacaMap.Modules.MapGenerator import MapGenerator


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
    data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\joined_data.csv"

    map_generator = MapGenerator(data_path=data_path, latitude=45.5236, longitude=-122.6750, zoom_start=13)
    map = map_generator.generate_map()
    return render(request, 'map.html', {'map': map._repr_html_()})
