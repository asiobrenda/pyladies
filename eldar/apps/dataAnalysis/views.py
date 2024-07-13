from django.shortcuts import render
from .upload_excelfiles import PFiles
from .models import Source, Product, YearData

def home(request):
    varx = 'WELCOME TO DATA ANALYSIS'
    source_ = Source.objects.all
    product = Product.objects.all()
    years = YearData.objects.values_list('year', flat=True)
    #print(years)

    return render(request, 'dataAnaysis/index.html', {'varx':varx, 'source':source_,
                                                      'product':product, 'years': years})

def upload_data(request):
    varx = "Data uploaded successfully"
    file_dirs = PFiles()
    #print(file_dirs)
    file_dirs.process_excel_files()
    return render(request, 'Ueconomics/load_data.html', {'varx': varx})