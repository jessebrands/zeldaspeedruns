from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User, Profile


def delete_fields(fields, needles=("first_name", "last_name")):
    return tuple(f for f in fields if f not in needles)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    fieldsets = (
        (None, {"fields": ('username', 'password', 'email')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ('username', 'display_name', 'email', 'is_staff')
    search_fields = ('username', 'profile__display_name', 'email')


admin.site.register(User, UserAdmin)
