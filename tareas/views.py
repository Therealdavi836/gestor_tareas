# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages
from .models import Tarea
from .forms import TareaForm
from django.utils import timezone

def lista_tareas(request):
    tareas_pendientes = Tarea.objects.filter(completada=False).order_by('fecha_limite')
    tareas_completadas = Tarea.objects.filter(completada=True).order_by('fecha_limite')

    form = TareaForm()
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea creada exitosamente!')
            return redirect('lista_tareas')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')

    return render(request, 'tareas/index.html', {
        'form': form,
        'tareas_pendientes': tareas_pendientes,
        'tareas_completadas': tareas_completadas,
        'now': timezone.now(),
    })

def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.save()
    messages.success(request, f'Tarea "{tarea.nombre}" marcada como completada!')
    return redirect('lista_tareas')

def borrar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    nombre_tarea = tarea.nombre
    tarea.delete()
    messages.success(request, f'Tarea "{nombre_tarea}" eliminada correctamente!')
    return redirect('lista_tareas')

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tarea actualizada correctamente!')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'tareas/editar_tarea.html', {
        'form': form,
        'tarea': tarea,
    })

def revertir_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = False
    tarea.save()
    messages.success(request, f'Tarea "{tarea.nombre}" marcada como pendiente nuevamente!')
    return redirect('lista_tareas')

class DetalleTareaView(DetailView):
    model = Tarea
    template_name = 'tareas/detalle_tarea.html'
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context