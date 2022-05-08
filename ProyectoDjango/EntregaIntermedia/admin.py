from atexit import register
from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(genUser)
admin.site.register(genItem)
admin.site.register(genVehicle)
admin.site.register(genAdmin)
