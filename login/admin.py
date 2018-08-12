'''
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from login.models import ScoutGroup
# Register your models here.

class ScoutGroupInline(admin.StackedInline):
	model = ScoutGroup
	can_delete = False
	verbose_name_plural = 'troop'

class UserAdmin(BaseUserAdmin):
	inlines = (ScoutGroupInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''