from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class BookAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'phone_number', )
    list_filter = ('first_name', 'last_name', 'email', )
    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone_number')