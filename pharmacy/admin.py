from django.contrib import admin
from pharmacy.models import Pharmacy, Drug, Manufacturer, PharmGroup, Country, Client

# Register your models here.

admin.site.register(Pharmacy)
admin.site.register(Drug)
admin.site.register(Manufacturer)
admin.site.register(PharmGroup)
admin.site.register(Country)
admin.site.register(Client)

