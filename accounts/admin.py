from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import MyUser


# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None,
         {'fields': ('username', 'password')}
         ),
        (_("Personal info"), {"fields": ("first_name","last_name","email","mc_number", "user_birthday", "pet_id", "pet_name", "pet_birthday")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(MyUser, MyUserAdmin)