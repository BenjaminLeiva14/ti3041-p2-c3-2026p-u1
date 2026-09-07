from django.shortcuts import render
from .models import Visita

def visita_list(request):
 visitas = Visita.objects.all()
 return render(request, 'visita/lista.html', {'visitas': visitas})