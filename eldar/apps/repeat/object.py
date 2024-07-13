from ..core.process_data import File

class PFiles(File):
     def __init__(self):
       super().__init__(file_name = 'repeat_app', target_field=None)

     def process_excel_files(self):
         df_imports = self.process_excel_data('imports')
         df_exports = self.process_excel_data('exports')
