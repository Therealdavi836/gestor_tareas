# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Tarea(models.Model):
    OPCIONES_PRIORIDAD = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    asignatura = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    completada = models.BooleanField(default=False)
    prioridad = models.CharField(
        max_length=5,
        choices=OPCIONES_PRIORIDAD,
        default='Media'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    archivo = models.FileField(upload_to='tareas/', null=True, blank=True, verbose_name="Archivo adjunto")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['fecha_limite']

    def __str__(self):
        return self.nombre

    @property
    def esta_atrasada(self):
        return not self.completada and self.fecha_limite < timezone.now().date()

    def get_absolute_url(self):
        return reverse('detalle_tarea', args=[str(self.id)])