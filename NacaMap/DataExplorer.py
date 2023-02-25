import geopandas as gpd
import pandas as pd

# Replace shapefile_path with the actual path to your shapefile
shapefile_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\CensusTracts\Oregon\tl_2022_41_tract.shp"

# Read the shapefile into a geopandas dataframe
gdf = gpd.read_file(shapefile_path)

# Replace income_data_path with the actual path to your income data CSV file
income_data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\Income\ACSST5Y2021.S1903-Data_new.csv"

# Read the income data CSV file into a pandas dataframe
income_df = pd.read_csv(income_data_path)
income_df = income_df.rename(columns={"GEO_ID": "GEOID"})

# Join the shapefile and the income data by the "GEOID" column
joined_df = gdf.merge(income_df, on="GEOID")

# Make sure that both datasets have the same coordinate reference system (CRS)
# In this example, we assume that the CRS of the shapefile is EPSG:4326
# and we set the CRS of the joined dataframe to EPSG:4326 as well
joined_df = joined_df.to_crs(epsg=4326)

file_path=r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\joined_data.csv"

# Save the new dataset as a CSV to the same folder path as the original CSV
joined_df.to_csv(file_path, index=False)

print("New CSV saved to:", file_path)