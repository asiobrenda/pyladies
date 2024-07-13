from django.shortcuts import render
from django.apps import apps as django_apps
from django.db import connection
from django.http import HttpResponse


def home(request):
    varx = 'WELCOME TO CORE APP'
    return render(request, 'core/index.html', {'varx':varx})


def truncate_skills(request, table_name,app_label):
    if request.user.is_staff:
        try:
            # Get the model class associated with the table name
            model_class = django_apps.get_model(app_label=app_label, model_name=table_name)

            # Truncate the table associated with the model
            with connection.cursor() as cursor:
                cursor.execute(f'TRUNCATE TABLE {model_class._meta.db_table} RESTART IDENTITY CASCADE')

            return HttpResponse(f'{table_name} table truncated successfully.')
        except LookupError:
            return HttpResponse(f'Table {table_name} not found.', status=404)
    else:
        return HttpResponse("Permission denied.", status=403)