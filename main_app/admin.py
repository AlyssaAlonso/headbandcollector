from django.contrib import admin
# import your models here
from .models import Headband, Status

# Register your models here
admin.site.register(Headband)
admin.site.register(Status)