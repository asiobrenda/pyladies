from ..core.process_data import File
from .models import Source, Product, YearData
import pandas as pd
class PFiles(File):
     def __init__(self):
       super().__init__(file_name ='excel_file', target_field=None)

     def process_excel_files(self):
        df_imports = self.process_excel_data('imports')
        df_exports = self.process_excel_data('exports')
        print(df_exports.shape)

        source_imports, created = Source.objects.get_or_create(type='imports')
        if created:
            for index, row in df_imports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for y in range(2015, 2020):
                 Y = 'Y' + str(y)
                 v = row[Y]
                 yd, created = YearData.objects.get_or_create(source=source_imports, product=product, year=y, values=v)

        source_exports, created = Source.objects.get_or_create(type='exports')
        if created:
            for index, row in df_exports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)

                for y in range(2015, 2020):
                    Y = 'Y' + str(y)
                    v = row[Y]
                    yd, created = YearData.objects.get_or_create(source=source_exports, product=product, year=y,
                                                                 values=v)