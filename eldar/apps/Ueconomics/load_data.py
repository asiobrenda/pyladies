from ..core.data_processing import Algo
from.models import Source, Product, YearData
import pandas as pd
class AlgoUE(Algo):
    def __init__(self):
        super().__init__(chapter_id='ueconomics', target_field=None)

    def upload_data_to_database(self):
        df_imports = self.process_excel_data('imports')
        df_exports = self.process_excel_data('exports')

        source_exports, created = Source.objects.get_or_create(type='exports')
        print(source_exports.type)
        print(created)
        if (created):
            for index, row in df_exports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_exports, product=product, year=ny,
                                                                 value=v)

        source_imports, created = Source.objects.get_or_create(type='imports')
        print(source_imports.type)
        print(created)
        if (created):
            for index, row in df_imports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_imports, product=product, year=ny,
                                                                 value=v)








