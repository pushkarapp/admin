from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    #list_display = [field.name for field in Category._meta.get_fields()]

    class Meta:
        model = Category


@admin.register(Label)
class LabelAdmin(ImportExportModelAdmin):
    #list_display = [field.name for field in Label._meta.get_fields()]

    class Meta:
        model = Label

@admin.register(Tags)
class TagsAdmin(ImportExportModelAdmin):
    #list_display = [field.name for field in Tags._meta.get_fields()]

    class Meta:
        model = Tags


