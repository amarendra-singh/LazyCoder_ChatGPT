from django.contrib import admin
from . models import Profile, Code,User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=('email', 'username','firstname', 'lastname')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Code)