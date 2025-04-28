from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'asignatura', 'fecha_limite', 'prioridad', 'archivo']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nombre': 'Nombre de la tarea',
            'descripcion': 'Descripción',
            'asignatura': 'Asignatura',
            'fecha_limite': 'Fecha límite',
            'prioridad': 'Prioridad',
            'archivo': 'Archivo adjunto',
        }