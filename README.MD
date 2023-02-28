
## Getting Started

`pip install -r requirements.txt`

`python manage.py runserver`

Browse to http://127.0.0.1:8000/map/


## Compile Other States' Shapefile

Edit the main function in `DataExplorer.py` to point at the new state's census tract shapefile and run it to generate new data source for the map page. Median income data and metropolitan stasticial area shapefiles included with repo from 2021 in the data folder and have entries for the whole US.   

[US Census Tract Shape Files by State](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2022&layergroup=Census+Tracts)

Currently only doing Oregon for performance.


### Sources

[US CBSA / MSA shape file](https://www.census.gov/geographies/reference-maps/2018/geo/cbsa.html)

[Median Income Census Data](https://data.census.gov/map?q=Income+and+Poverty&tid=ACSST1Y2021.S1903&layer=VT_2021_040_00_PP_D1&mode=thematic&loc=43.3751,-113.1138,z1.4027)


