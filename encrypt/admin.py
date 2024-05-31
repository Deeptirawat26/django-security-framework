from django.contrib import admin
from .models import EncryptedFile

@admin.register(EncryptedFile)
class EncryptedFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'username', 'upload_date')
