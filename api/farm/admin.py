from django.contrib import admin
from .models import Crop,Farmer,FarmType,User

admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(FarmType)
admin.site.register(User)
