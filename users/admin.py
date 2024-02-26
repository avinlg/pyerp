from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Admin
from .models import User

class UserAdmin(Admin):
    list_display = ["date_joined", "username", "first_name", "last_name"]
    model = User

    fieldsets = Admin.fieldsets
    # fieldsets = Admin.fieldsets + (
    #     (
    #         "Extra Fields",
    #         {
    #             "fields": (
    #                 "email",
    #             )
    #         },
    #     ),
    # )

admin.site.register(User, UserAdmin)