from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )


@admin.register(CategoryPro)
class CategoryProAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(ProfilePro)
class ProfileProeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.register(CommentPro)
class CommentProeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )



