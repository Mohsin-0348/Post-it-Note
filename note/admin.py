from django.contrib import admin
from .models import *

admin.site.register(Note)
admin.site.register(Nk)
admin.site.register(Jo)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'is_active', 'password', 're_password')


admin.site.register(Users, UsersAdmin)
