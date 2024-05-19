from django.contrib import admin
from .models import tudoapp
class user(admin.ModelAdmin):
    list_display=('name','email','mob','password')
admin.site.register(tudoapp,user)

# Register your models here.
