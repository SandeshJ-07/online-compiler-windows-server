from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Pratice_Problems)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(User_Pratice_Solution)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(All_Contest_Data)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Contest_Questions)
class ViewAdmin(ImportExportModelAdmin):
    pass