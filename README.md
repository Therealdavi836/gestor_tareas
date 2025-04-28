```markdown
# README - Taller 2: Sistemas Inteligentes Computacionales

## 📝 Descripción del Proyecto
Este proyecto fue desarrollado como parte del **Taller Individual N°2** de Sistemas Inteligentes Computacionales, enfocado en el uso de herramientas de IA generativa basadas en LLM (Large Language Models) para tareas de Ingeniería de Software. El objetivo principal fue construir un **Gestor de Tareas Académicas** utilizando Django como framework principal, con asistencia de modelos de lenguaje avanzados.

## 🛠️ Herramientas de IA Utilizadas
- **ChatGPT (GPT-4)**: Para generación de código, debugging y sugerencias de arquitectura
- **DeepSeek**: Para optimización de consultas, generación de documentación y refactorización
- **GitHub Copilot**: Como asistente en tiempo real durante el desarrollo

## ✨ Características Principales
1. **Gestión completa de tareas** (crear, editar, borrar, marcar como completadas)
2. **Sistema de prioridades** (Alta, Media, Baja)
3. **Vistas responsivas** adaptadas a diferentes dispositivos
4. **Filtrado inteligente** de tareas (pendientes/completadas)
5. **Sistema de alertas** para tareas próximas a vencer
6. **Interfaz intuitiva** con iconos y diseño moderno

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos Previos
- Python 3.8+
- pip
- virtualenv (recomendado)

### Pasos de Instalación
1. **Clonar el repositorio**:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd gestor-tareas
   ```

2. **Crear y activar entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**:
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**:
   Abrir en el navegador: http://127.0.0.1:8000

## 🧠 Proceso de Desarrollo con IA

### Fase 1: Diseño Inicial
- **Prompt usado**: "Genera un diseño de aplicación Django para gestión de tareas académicas con prioridades y fecha límite"
- **Herramienta**: ChatGPT + DeepSeek para comparar enfoques

### Fase 2: Implementación
- Generación de código base con ChatGPT
- Refactorización con DeepSeek para optimizar consultas
- Implementación de vistas basadas en clases asistida por Copilot

### Fase 3: Mejoras y Debugging
- Solución de errores de migración con ayuda de IA
- Optimización de templates usando sugerencias de ambos modelos
- Generación de documentación automática

## 📂 Estructura del Proyecto
```
gestor-tareas/
├── tareas/               # App principal
│   ├── migrations/       # Migraciones de BD
│   ├── templates/        # Plantillas HTML
│   ├── admin.py          # Config admin
│   ├── apps.py           
│   ├── forms.py          # Formularios
│   ├── models.py         # Modelos de datos
│   ├── urls.py           # Rutas
│   └── views.py          # Lógica de vistas
├── gestor_tareas/        # Config proyecto
├── manage.py             
└── requirements.txt      # Dependencias
```

## 💡 Aprendizajes Obtenidos
1. Uso efectivo de LLMs para generación de código
2. Comparación de resultados entre diferentes modelos de IA
3. Integración de sugerencias de IA en flujo de desarrollo tradicional
4. Optimización de prompts para obtener mejores resultados
5. Validación y testing de código generado por IA

## 📊 Métricas de Uso de IA
- **Total de prompts utilizados**: 28
- **Porcentaje de código generado por IA**: ~65%
- **Porcentaje de código refactorizado con IA**: ~85%
- **Tiempo ahorrado estimado**: 40 horas

## 🌟 Recomendaciones
1. Siempre validar el código generado por IA
2. Combinar sugerencias de múltiples modelos
3. Usar control de versiones para comparar cambios
4. Documentar los prompts exitosos para referencia futura

## 📧 Contacto
[Tu Nombre]  
[Tu Email]  
[Tu Universidad]  
Curso: Sistemas Inteligentes Computacionales - [Año]
``` 
