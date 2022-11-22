from django.contrib import admin
from .models import Map
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Map)
class MapData(ImportExportModelAdmin):
    pass