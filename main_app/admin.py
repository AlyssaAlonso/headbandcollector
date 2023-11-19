from django.contrib import admin
# import your models here
from .models import Headband, Status, Accessory

# Register your models here
admin.site.register(Headband)
admin.site.register(Status)
admin.site.register(Accessory)