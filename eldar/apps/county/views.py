from django.shortcuts import render
from .process_trial_excel import CFiles
from.models import County

def home(request):
    varx = "A LIST OF UGANDAN DISTRICTS"
    county = County.objects.all()
    return render(request, 'county/index.html', {'varx':varx, 'county':county})


def upload_data(request):
    varx = "Data uploaded successfully"
    file_dirs = CFiles()
    #print(file_dirs)
    file_dirs.process_district_files()
    return render(request, 'county/load_data.html', {'varx': varx})