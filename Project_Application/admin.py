from django.contrib import admin
from Project_Application.models import Manager
# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
    list_display=['email','firstname','lastname','password','address','dateofbirth','company']
admin.site.register(Manager, ManagerAdmin)
