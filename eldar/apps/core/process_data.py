import os

import pandas as pd
from django.conf import settings

class File(object):
     def __init__(self, file_name, target_field):
         self.FILE_NAME = file_name
         # self.TARGET_FIELD = None

     #Create directories to be part of django project

         self.DJANGO_PROJECT_ROOT = os.path.join(settings.ELDAR_DIR, "files", self.FILE_NAME)
         os.makedirs(self.DJANGO_PROJECT_ROOT, exist_ok=True)

         self.EXCEL_PATH =os.path.join(self.DJANGO_PROJECT_ROOT, "excel_files")
         os.makedirs(self.EXCEL_PATH, exist_ok=True)
         #print(s_path)


         self.DATA = None
         self.TARGET_FIELD = None


     def process_excel_data(self, excel_file):
         file_path = os.path.join(self.EXCEL_PATH, excel_file + '.xlsx')
         self.DATA = pd.read_excel(file_path)
         return self.DATA


