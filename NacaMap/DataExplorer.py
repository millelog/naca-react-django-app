import pandas as pd

# Replace file_path with the actual path to your CSV file
file_path = r"C:\Users\mille\PycharmProjects\naca-react-django-app\NacaMap\data\Income\ACSST5Y2021.S1903-Data.csv"

# Read the CSV file into a pandas dataframe
df = pd.read_csv(file_path)

# Find the column that contains "median income" in its title
median_income_col = None
for col in df.columns:
    print(col)
    if "median" in col.lower():
        median_income_col = col
        break

# Check if a column containing "median income" was found
if median_income_col is not None:
    # Select the column containing "median income" into a new dataframe
    median_income_df = df[[median_income_col]]
    print("Selected column:", median_income_col)
    print(median_income_df.head())
else:
    print("No column containing 'median income' was found.")
