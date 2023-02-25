from django.shortcuts import render
import folium
import pandas as pd
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
    joined_data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\Income\ACSST5Y2021.S1903-Data_new.csv"

    # Read the joined dataset into a pandas dataframe
    joined_df = pd.read_csv(joined_data_path)

    joined_df.dropna()

    joined_df = joined_df.loc[~(joined_df['MedianIncome'].isna())]

    map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Add the joined dataset as a choropleth layer
    folium.Choropleth(
        geo_data=joined_df,
        data=joined_df,
        columns=["GEO_ID", "MedianIncome"],
        key_on="feature.properties.GEOID",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Median Income",
        highlight=True,
        name="Median Income",
        overlay=True
    ).add_to(map)

    map = map._repr_html_() # render map as HTML
    return render(request, 'map.html', {'map': map})
