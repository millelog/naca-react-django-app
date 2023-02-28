import geopandas as gpd
import pandas as pd
from shapely import wkt


def ComputeSpatialDataFrame(Tract_shapefile_path):
    CBSAFP_shapefile_path = r'.\data\CBSA500k\cb_2018_us_cbsa_500k.shp'
    income_data_path = r".\data\Income\ACSST5Y2021.S1903-Data_new.csv"
    # Read in the shapefiles
    msa = gpd.read_file(CBSAFP_shapefile_path)
    tract = gpd.read_file(Tract_shapefile_path)

    # Spatial join to get the CBSAFP id for each census tract
    tracts_with_cbsafp = gpd.sjoin(tract, msa[['CBSAFP', 'geometry']], how='left', op='intersects')

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
    median_median_income = joined_df.groupby('CBSAFP')['MedianIncome'].median()

    # Add a new column to joined_df with the average median income for each row's CBSAFP
    joined_df['CBSAMedianIncome'] = joined_df['CBSAFP'].map(median_median_income)
    joined_df['CBSAMedianIncome'].fillna(-1, inplace=True)
    joined_df['CBSAMedianIncome'] = joined_df['CBSAMedianIncome'].astype(int)

    # Add a new column to joined_df with the color for each row based on the MedianIncome and CBSAMedianIncome values
    joined_df['color'] = joined_df.apply(lambda x: '#808080' if pd.isna(x['MedianIncome']) or pd.isna(x['CBSAMedianIncome']) else ('#0000ff' if x['MedianIncome'] < x['CBSAMedianIncome'] else '#ff0000'), axis=1)
    joined_df = joined_df.to_crs(epsg=4326)


    file_path = r".\data\final_data.shp"

    # Save the new dataset as a CSV to the same folder path as the original CSV
    joined_df.to_file(file_path, driver='GeoJSON')

    print("New shape file saved to:", file_path)

def main():
    Tract_shapefile_path = r'.\data\CensusTracts\Oregon\tl_2022_41_tract.shp'
    ComputeSpatialDataFrame(Tract_shapefile_path)

if __name__ == '__main__':
    main()

