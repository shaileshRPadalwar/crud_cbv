from django.contrib import admin
from .models import Company
# Register your models here.

@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display=['name','location','ceo']


