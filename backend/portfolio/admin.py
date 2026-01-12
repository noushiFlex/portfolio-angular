from django.contrib import admin
from .models import Experience, Service, Projet, PriseDeContact, Localisation

# Register your models here.
admin.site.register(Experience)
admin.site.register(Service)
admin.site.register(Projet)
admin.site.register(PriseDeContact)
admin.site.register(Localisation)