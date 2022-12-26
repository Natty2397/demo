from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('companies_name', 'first_name', 'last_name','Title', 'Email', 'url')