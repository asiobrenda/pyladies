from ..core.data_processing import Algo
from .models import County, CountyValue
import pandas as pd
import numpy as np
class CFiles(Algo):
    def __init__(self):
        super().__init__(chapter_id='country_excel_file', target_field=None)

    def process_district_files(self):
        df_county = self.process_excel_data('Trial_excel')

        # Print the columns to check for the existence of 'District'
        print(df_county.columns)

        for index, row in df_county.iterrows():
            try:
                county_name = row['District ']  # Ensure that the column name is case-sensitive
                county, created = County.objects.get_or_create(country=county_name)
            except KeyError as ee:
                print(ee)
                continue  # Skip the rest of the loop for this row if 'District' is not found

            for year in range(2012, 2018):
                try:
                    value = row[year]
                    print("Processing" + county_name, "-" + year + "-" + "Value:", value)

                    if value == '-':
                        value = None
                    elif pd.isna(value):  # Check for null values explicitly using pandas isna()
                        value = None

                    print("Setting value to:", value)

                    CountyValue.objects.get_or_create(county=county, years=year, value_data=value)
                except KeyError as ee:
                    pass
