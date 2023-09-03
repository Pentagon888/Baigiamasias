# Grostena_app/admin.py

from django.contrib import admin
from .models import RepairCategory, AutoService

admin.site.register(RepairCategory)
admin.site.register (AutoService)