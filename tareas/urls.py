from django.urls import path
from .views import lista_tareas, completar_tarea, borrar_tarea, editar_tarea, revertir_tarea, DetalleTareaView

urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),
    path('completar/<int:tarea_id>/', completar_tarea, name='completar_tarea'),
    path('borrar/<int:tarea_id>/', borrar_tarea, name='borrar_tarea'),
    path('editar/<int:tarea_id>/', editar_tarea, name='editar_tarea'),
    path('tarea/<int:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'),
    path('revertir/<int:tarea_id>/', revertir_tarea, name='revertir_tarea'),
]