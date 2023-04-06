from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("email", "password", "is_active")


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (

        (None, {'fields': ('email', 'password', )}),

        (_('Personal info'), {'fields': ('first_name', 'last_name')}),

        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',

                                       'groups', 'user_permissions')}),

        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),

        (_('user_info'), {
         'fields': ('title', 'phone_no', "courses_handled", "faculty")}),

    )

    add_fieldsets = (
        (None, {

            'classes': ('wide', ),

            'fields': ('email', 'password1', 'password2'),

        }),
    )

    list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone_no"]

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('email', )


admin.site.register(User, UserAdmin)
