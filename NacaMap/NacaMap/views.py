from django.shortcuts import render
import folium
import pandas as pd
import geopandas as gpd
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
    # Replace joined_data_path with the actual path to your joined dataset
    joined_data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\joined_data.csv"
    # Read the joined dataset into a pandas dataframe
    df = pd.read_csv(joined_data_path)

    # Convert the dataframe to a geopandas dataframe and set the geometry column
    gdf = gpd.GeoDataFrame(df, geometry='geometry')

    map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Create a GeoJson layer using the 'geometry' and 'MedianIncome' columns
    folium.GeoJson(
        data=gdf[['geometry', 'MedianIncome']].to_json(),
        name='GeoJson',
        style_function=lambda feature: {
            'fillColor': '#ff0000' if feature['properties']['MedianIncome'] > 50000 else '#0000ff',
            'color': '#000000',
            'weight': 1,
            'fillOpacity': 0.7,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['MedianIncome'],
            aliases=['Median Income'],
            labels=True,
            sticky=False
        ),
        highlight_function=lambda feature: {
            'fillColor': '#00ff00',
            'color': '#000000',
            'weight': 3,
            'fillOpacity': 0.7,
        }
    ).add_to(map)

    # Add a layer control to the map
    folium.LayerControl().add_to(map)

    map = map._repr_html_() # render map as HTML
    return render(request, 'map.html', {'map': map})
