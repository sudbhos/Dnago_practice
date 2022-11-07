from django.contrib import admin
from .models import employee
# Register your models here.

class Adminemp(admin.ModelAdmin):
    list_display = ["name","surname","salary","location","empid"]

admin.site.register(employee,Adminemp)
