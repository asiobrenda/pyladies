import os
from django.conf  import settings
import pandas as pd

class Algo(object):
      def __init__(self, chapter_id, target_field):
           self.CHAPTER_ID = chapter_id

           #Create directories to make it pasrt of django project

           self.PROJECT_ROOT_DIR = os.path.join(settings.ELDAR_DIR, "data", self.CHAPTER_ID)
           os.makedirs(self.PROJECT_ROOT_DIR, exist_ok=True)

           self.DATA_PATH = os.path.join(self.PROJECT_ROOT_DIR, "datasets")
           os.makedirs(self.DATA_PATH, exist_ok=True)

           self.TARGET_FIELD = target_field
           self.DATA = None

      def process_excel_data(self, file):
          excel_path = os.path.join(self.DATA_PATH, file + '.xlsx')
          self.DATA = pd.read_excel(excel_path)
          return self.DATA











