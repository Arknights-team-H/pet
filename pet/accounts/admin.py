from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import HospitalUser

class HospitalUserAdmin(UserAdmin):
    fieldsets = (
        (None,
         {'fields':('username', 'password')}
         ),
        (_('Personal info'),{'fields':('first_name','last_name','email','hospital_id','hospital_name','address','phone_number','director_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'),{'fields':('last_login','date_joined')}),
    )
admin.site.register(HospitalUser,HospitalUserAdmin)