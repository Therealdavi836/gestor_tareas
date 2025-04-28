# 📚 Gestor de Tareas Académicas - Taller 2 (Django)

## 📌 Descripción
Ésta aplicación fue desarrollado como parte del **Taller Individual N°2** del curso **Sistemas Inteligentes Computacionales**. El objetivo fue construir un **Gestor de Tareas Académicas** utilizando **Django** como framework principal, asistido por herramientas de **IA generativa** basadas en **LLM (Large Language Models)** para apoyar el desarrollo de software.

## 🚀 Características
- 🔹 **Gestión completa de tareas**: Crear, editar, borrar, marcar como completadas.
- 🔹 **Sistema de prioridades**: Alta, Media y Baja.
- 🔹 **Vistas responsivas**: Adaptadas a diferentes dispositivos.
- 🔹 **Filtrado inteligente**: Ver tareas pendientes y completadas.
- 🔹 **Sistema de alertas**: Para tareas próximas a vencer.
- 🔹 **Interfaz intuitiva**: Diseño moderno y fácil de usar.

## 🛠️ Herramientas de IA Utilizadas
- **ChatGPT (GPT-4)**: Generación de código, debugging y arquitectura.
- **DeepSeek**: Optimización de consultas, generación de documentación y refactorización.
- **GitHub Copilot**: Asistente en tiempo real durante el desarrollo.

## 📂 Estructura del Proyecto
```
📦 gestor-tareas
 ┣ 📂 tareas
 ┃ ┣ 📂 migrations (Migraciones de base de datos)
 ┃ ┣ 📂 templates (Plantillas HTML)
 ┃ ┣ 📜 admin.py (Configuración del admin)
 ┃ ┣ 📜 apps.py (Configuración de la app)
 ┃ ┣ 📜 forms.py (Formularios de tareas)
 ┃ ┣ 📜 models.py (Modelos de datos)
 ┃ ┣ 📜 urls.py (Rutas de la app)
 ┃ ┗ 📜 views.py (Lógica de vistas)
 ┣ 📂 gestor_tareas (Configuración general del proyecto)
 ┣ 📜 manage.py
 ┗ 📜 requirements.txt (Dependencias del proyecto)
```

## ⚡ Instalación
1. Clona este repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd gestor-tareas
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
5. (Opcional) Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
6. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
7. Accede a la aplicación:
   ```
   http://127.0.0.1:8000
   ```

## 🧠 Proceso de Desarrollo con IA
- **Fase 1: Diseño Inicial**  
  ➡️ Prompt: *"Genera un diseño de aplicación Django para gestión de tareas académicas con prioridades y fecha límite."*  
  ➡️ Herramientas: ChatGPT y DeepSeek.

- **Fase 2: Implementación**  
  ➡️ Código base con ChatGPT, refactorizado con DeepSeek.  
  ➡️ Implementación de vistas basadas en clases con apoyo de Copilot.

- **Fase 3: Mejoras y Debugging**  
  ➡️ Corrección de errores de migración.  
  ➡️ Optimización de templates y generación de documentación automática.

## 📊 Métricas de Uso de IA
- **Total de prompts utilizados**: 28
- **Porcentaje de código generado por IA**: ~65%
- **Porcentaje de código refactorizado con IA**: ~85%
- **Tiempo ahorrado estimado**: 40 horas

## 💡 Aprendizajes Obtenidos
- Uso efectivo de modelos de lenguaje para generación de código.
- Comparación crítica entre resultados de distintos modelos de IA.
- Mejora de habilidades en prompting y refinamiento de solicitudes.
- Integración de herramientas de IA en el flujo de desarrollo tradicional.
- Validación rigurosa y testing del código generado.

## 🌟 Recomendaciones
- ✅ Validar siempre el código generado por IA.
- ✅ Comparar sugerencias de múltiples modelos de IA.
- ✅ Utilizar control de versiones para gestionar cambios.
- ✅ Documentar los mejores prompts para futuras referencias.

## 📧 Contacto
Este proyecto fue desarrollado para fines académicos en la materia de **Sistemas Inteligentes Computacionales**.  
- Juan David Fajardo Betancourt
- jfajardob@unal.edu.co
- Universidad Nacional de Colombia Sede-Manizales

---
💡 *Contribuciones y sugerencias son bienvenidas.* 🚀

---
