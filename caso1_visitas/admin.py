from django.contrib import admin
from .models import Visita

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "motivo_visita", "fecha", "hora_entrada")
    search_fields = ("nombre", "motivo_visita", "rut__exact")
    list_filter = ("fecha",)
    ordering = ("-fecha", "-hora_entrada")
    list_per_page = 25
    autocomplete_fields = () 
