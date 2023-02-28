import folium
import pandas as pd
import geopandas as gpd
from shapely import wkt


class MapGenerator:
    def __init__(self, data_path: str, latitude: float, longitude: float, zoom_start: int = 10):
        self.data_path = data_path
        self.latitude = latitude
        self.longitude = longitude
        self.zoom_start = zoom_start

    def style_function(self, feature):
        median_income = feature['properties'].get('MedianIncome')
        if median_income is None:
            return {
                'fillColor': '#808080',  # gray
                'color': '#000000',
                'weight': 1,
                'fillOpacity': 0.7,
            }
        else:
            return {
                'fillColor': '#ff0000' if median_income > 50000 else '#0000ff',
                'color': '#000000',
                'weight': 1,
                'fillOpacity': 0.7,
            }

    def generate_map(self) -> folium.Map:

        # Read the joined dataset into a pandas dataframe
        df = pd.read_csv(self.data_path)

        # Convert the WKT strings in the geometry column to Shapely objects
        df['geometry'] = df['geometry'].apply(wkt.loads)

        # Convert the dataframe to a geopandas dataframe and set the geometry column
        gdf = gpd.GeoDataFrame(df, geometry='geometry')

        map = folium.Map(location=[self.latitude, self.longitude], zoom_start=self.zoom_start)

        # Create a GeoJson layer using the 'geometry' and 'MedianIncome' columns
        folium.GeoJson(
            data=gdf[['geometry', 'MedianIncome']].to_json(),
            name='GeoJson',
            style_function=self.style_function,
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
        return map
