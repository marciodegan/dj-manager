from django.contrib import admin

from .models import File, FileLancamento, FileDate

admin.site.register(File)
admin.site.register(FileLancamento)
admin.site.register(FileDate)
