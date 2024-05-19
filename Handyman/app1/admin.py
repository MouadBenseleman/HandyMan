from django.contrib import admin
from .models import Client, MaintenanceTechnician,Contact

# Register your models here.
admin.site.register(Client)
admin.site.register(MaintenanceTechnician)
admin.site.register(Contact)
