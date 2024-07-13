from ..core.data_processing import Algo
from .models import CDistrict, DistrictValue
import pandas as pd
class AlgoUE(Algo):
    def __init__(self):
        super().__init__(chapter_id='ueconomics', target_field=None)

    def process_excel_files(self):
        df_district = self.process_excel_data('Trial_excel')

        for index, row in df_district.iterrows():

                district_name_ = row['District ']  # Ensure that the column name is case-sensitive
                district, created = CDistrict.objects.get_or_create(district_name=district_name_)

                for year in range(2012, 2018):
                    value = row[year]
                    #print("Processing" + '', district_name_, "-" + '', str(year), '' + "-", '' + "Value:", value)

                    if value == '-':
                        value = str(0)
                    else:
                        value = 0


                    #print("Setting value to:", value)

                    DistrictValue.objects.get_or_create(district_name=district, year=year, district_value=value)
