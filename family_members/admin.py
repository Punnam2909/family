from django.contrib import admin
from .models import Punnam
# Register your models here.

class PunnamAdmin(admin.ModelAdmin):
    list_display = ("id","Name","Description","kids",)
    list_display_links = ("Name",)


admin.site.register(Punnam,PunnamAdmin)

