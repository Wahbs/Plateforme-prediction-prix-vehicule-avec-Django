from django.contrib import admin
from prix_voiture.models import *

# Register your models here.

class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'annee')


admin.site.register(details_voiture, VoitureAdmin)