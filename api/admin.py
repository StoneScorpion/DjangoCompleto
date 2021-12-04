from django.contrib import admin
from .models import Client, Medicine, Service
# Register your models here.
admin.site.register(Client)
admin.site.register(Medicine)
admin.site.register(Service)
