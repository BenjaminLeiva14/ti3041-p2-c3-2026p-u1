from django.contrib import admin
from .models import Visita

# Register your models here.

class VisitaAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    ordering = ["nombre"]

admin.site.register(model_or_iterable=Visita, admin_class=VisitaAdmin)