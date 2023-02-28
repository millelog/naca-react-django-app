import geopandas as gpd
import pandas as pd

def JoinCensusTractWithIncomne():
    # Replace shapefile_path with the actual path to your shapefile
    shapefile_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\CensusTracts\Oregon\tl_2022_41_tract.shp"

    # Read the shapefile into a geopandas dataframe
    gdf = gpd.read_file(shapefile_path)
    gdf = gdf.dropna(subset=['geometry'])

    # Replace income_data_path with the actual path to your income data CSV file
    income_data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\Income\ACSST5Y2021.S1903-Data_new.csv"

    # Read the income data CSV file into a pandas dataframe
    income_df = pd.read_csv(income_data_path)
    income_df = income_df.rename(columns={"GEO_ID": "GEOID", "geometry": "income_geometry"})
    income_df['MedianIncome'] = pd.to_numeric(income_df['MedianIncome'], errors='coerce')

    # Remove the "1400000US" prefix from the GEOID column
    income_df["GEOID"] = income_df["GEOID"].str.replace("1400000US", "")

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

def ComputeSpatialDataFrame():
    CBSAFP_shapefile_path = r'C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\CBSA500k\cb_2018_us_cbsa_500k.shp'
    CensusTract_shapefile_path = r'C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\USTract\cb_2019_us_tract_500k.shp'
    income_data_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\Income\ACSST5Y2021.S1903-Data_new.csv"

    # Read in the shapefiles
    msa = gpd.read_file(CBSAFP_shapefile_path)
    tract = gpd.read_file(CensusTract_shapefile_path)

    # Spatial join to get the CBSAFP id for each census tract
    tracts_with_cbsafp = gpd.sjoin(tract, msa[['CBSAFP', 'geometry']], how='left', op='within')

    # Drop unnecessary columns
    tracts_with_cbsafp = tracts_with_cbsafp[['STATEFP', 'COUNTYFP', 'TRACTCE', 'CBSAFP', 'GEOID', 'geometry']]

    # Read the income data CSV file into a pandas dataframe
    income_df = pd.read_csv(income_data_path)
    income_df = income_df.rename(columns={"GEO_ID": "GEOID", "geometry": "income_geometry"})
    income_df['MedianIncome'] = pd.to_numeric(income_df['MedianIncome'], errors='coerce')

    # Remove the "1400000US" prefix from the GEOID column
    income_df["GEOID"] = income_df["GEOID"].str.replace("1400000US", "")

    # Join the shapefile and the income data by the "GEOID" column
    joined_df = tracts_with_cbsafp.merge(income_df, on="GEOID")

    # Compute the average median income for each CBSAFP
    avg_median_income = joined_df.groupby('CBSAFP')['MedianIncome'].mean()

    # Add a new column to joined_df with the average median income for each row's CBSAFP
    joined_df['CBSAMedianIncome'] = joined_df['CBSAFP'].map(avg_median_income)

    joined_df = joined_df.to_crs(epsg=4326)

    file_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\final_data.csv"

    # Save the new dataset as a CSV to the same folder path as the original CSV
    joined_df.to_csv(file_path, index=False)

    print("New CSV saved to:", file_path)

ComputeSpatialDataFrame()

