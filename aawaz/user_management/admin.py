from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserProfile, UserLavel,MemberBlocked


# Register your models here.
@admin.register(UserProfile)
class UserAdmin(ImportExportModelAdmin):
    
    list_display = [field.name for field in UserProfile._meta.get_fields()]
    #list_filter = ('user__username',)

    class Meta:
        model = UserProfile

@admin.register(UserLavel)
class UserLavelAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in UserLavel._meta.get_fields()]
    #list_filter = ('user__username',)

    class Meta:
        model = UserLavel


@admin.register(MemberBlocked)
class MemberBlockedAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in MemberBlocked._meta.get_fields()]
    #list_filter = ('user__username',)

    class Meta:
        model = MemberBlocked

