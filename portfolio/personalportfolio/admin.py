from django.contrib import admin
from .models import Projects,Certificates,Contacts

# Register your models here.
admin.site.register(Projects)
admin.site.register(Certificates)
admin.site.register(Contacts)