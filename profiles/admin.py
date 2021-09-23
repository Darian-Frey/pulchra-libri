from django.contrib import admin
from .models import WishList, UserProfile

# Register your models here.

class WishListInline(admin.TabularInline):
    model = WishList


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )

    inlines = [WishListInline, ]