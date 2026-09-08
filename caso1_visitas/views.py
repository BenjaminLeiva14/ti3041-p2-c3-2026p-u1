from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm

from django.views.decorators.csrf import csrf_protect

def visita_list(request):
 visitas = Visita.objects.all()
 return render(request, 'visita/lista_visita.html', {'object_list': visitas})

def visita_detail(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    return render(request, 'visita/detalle_visita.html', {'object': visita})

@csrf_protect
def visita_create(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visita_list')
    else:
        form = VisitaForm()
    return render(request, 'visita/formulario_visita.html', {'form': form})

@csrf_protect
def visita_update(request, pk):
    visita = get_object_or_404(Visita, pk=pk)

    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)

        if form.is_valid():
            form.save()
            return redirect('visita_list')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'visita/formulario_visita.html', {'form': form})

@csrf_protect
def visita_delete(request, pk):
    visita = get_object_or_404(Visita, pk=pk)

    if request.method == 'POST':
        visita.delete()
        return redirect('visita_list')

    return render(request, 'visita/confirmar_borrado.html', {'object': visita})