<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Taller 2: Sistemas Inteligentes Computacionales</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>

<div class="container mt-5">
    <h1 class="display-4">README - Taller 2: Sistemas Inteligentes Computacionales</h1>

    <section class="my-5">
        <h3>📝 Descripción del Proyecto</h3>
        <p>Este proyecto fue desarrollado como parte del <strong>Taller Individual N°2</strong> de Sistemas Inteligentes Computacionales, enfocado en el uso de herramientas de IA generativa basadas en LLM (Large Language Models) para tareas de Ingeniería de Software. El objetivo principal fue construir un <strong>Gestor de Tareas Académicas</strong> utilizando Django como framework principal, con asistencia de modelos de lenguaje avanzados.</p>
    </section>

    <section class="my-5">
        <h3>🛠️ Herramientas de IA Utilizadas</h3>
        <ul>
            <li><strong>ChatGPT (GPT-4)</strong>: Para generación de código, debugging y sugerencias de arquitectura</li>
            <li><strong>DeepSeek</strong>: Para optimización de consultas, generación de documentación y refactorización</li>
            <li><strong>GitHub Copilot</strong>: Como asistente en tiempo real durante el desarrollo</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>✨ Características Principales</h3>
        <ul>
            <li><strong>Gestión completa de tareas</strong> (crear, editar, borrar, marcar como completadas)</li>
            <li><strong>Sistema de prioridades</strong> (Alta, Media, Baja)</li>
            <li><strong>Vistas responsivas</strong> adaptadas a diferentes dispositivos</li>
            <li><strong>Filtrado inteligente</strong> de tareas (pendientes/completadas)</li>
            <li><strong>Sistema de alertas</strong> para tareas próximas a vencer</li>
            <li><strong>Interfaz intuitiva</strong> con iconos y diseño moderno</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>🚀 Cómo Ejecutar el Proyecto</h3>

        <h5>Requisitos Previos</h5>
        <ul>
            <li>Python 3.8+</li>
            <li>pip</li>
            <li>virtualenv (recomendado)</li>
        </ul>

        <h5>Pasos de Instalación</h5>
        <ol>
            <li><strong>Clonar el repositorio</strong>:
                <pre><code>git clone [URL_DEL_REPOSITORIO]
cd gestor-tareas</code></pre>
            </li>
            <li><strong>Crear y activar entorno virtual</strong>:
                <pre><code>python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows</code></pre>
            </li>
            <li><strong>Instalar dependencias</strong>:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Configurar la base de datos</strong>:
                <pre><code>python manage.py migrate</code></pre>
            </li>
            <li><strong>Crear superusuario (opcional)</strong>:
                <pre><code>python manage.py createsuperuser</code></pre>
            </li>
            <li><strong>Ejecutar el servidor</strong>:
                <pre><code>python manage.py runserver</code></pre>
            </li>
            <li><strong>Acceder a la aplicación</strong>:
                <p>Abrir en el navegador: <strong>http://127.0.0.1:8000</strong></p>
            </li>
        </ol>
    </section>

    <section class="my-5">
        <h3>🧠 Proceso de Desarrollo con IA</h3>

        <h5>Fase 1: Diseño Inicial</h5>
        <p><strong>Prompt usado</strong>: "Genera un diseño de aplicación Django para gestión de tareas académicas con prioridades y fecha límite"</p>
        <p><strong>Herramienta</strong>: ChatGPT + DeepSeek para comparar enfoques</p>

        <h5>Fase 2: Implementación</h5>
        <ul>
            <li>Generación de código base con ChatGPT</li>
            <li>Refactorización con DeepSeek para optimizar consultas</li>
            <li>Implementación de vistas basadas en clases asistida por Copilot</li>
        </ul>

        <h5>Fase 3: Mejoras y Debugging</h5>
        <ul>
            <li>Solución de errores de migración con ayuda de IA</li>
            <li>Optimización de templates usando sugerencias de ambos modelos</li>
            <li>Generación de documentación automática</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>📂 Estructura del Proyecto</h3>
        <pre><code>gestor-tareas/
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
└── requirements.txt      # Dependencias</code></pre>
    </section>

    <section class="my-5">
        <h3>💡 Aprendizajes Obtenidos</h3>
        <ul>
            <li>Uso efectivo de LLMs para generación de código</li>
            <li>Comparación de resultados entre diferentes modelos de IA</li>
            <li>Integración de sugerencias de IA en flujo de desarrollo tradicional</li>
            <li>Optimización de prompts para obtener mejores resultados</li>
            <li>Validación y testing de código generado por IA</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>📊 Métricas de Uso de IA</h3>
        <ul>
            <li><strong>Total de prompts utilizados</strong>: 28</li>
            <li><strong>Porcentaje de código generado por IA</strong>: ~65%</li>
            <li><strong>Porcentaje de código refactorizado con IA</strong>: ~85%</li>
            <li><strong>Tiempo ahorrado estimado</strong>: 40 horas</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>🌟 Recomendaciones</h3>
        <ul>
            <li>Siempre validar el código generado por IA</li>
            <li>Combinar sugerencias de múltiples modelos</li>
            <li>Usar control de versiones para comparar cambios</li>
            <li>Documentar los prompts exitosos para referencia futura</li>
        </ul>
    </section>

    <section class="my-5">
        <h3>📧 Contacto</h3>
        <p><strong>[Tu Nombre]</strong></p>
        <p><strong>[Tu Email]</strong></p>
        <p><strong>[Tu Universidad]</strong></p>
        <p>Curso: Sistemas Inteligentes Computacionales - <strong>[Año]</strong></p>
    </section>
</div>

</body>
</html>
