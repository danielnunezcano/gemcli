# GemCLI

Una interfaz de línea de comandos (CLI) interactiva para conversar con Google Gemini AI, diseñada para proporcionar una experiencia de chat enriquecida con soporte multimodal y gestión de conversaciones.

## 🚀 Características Principales

### 💬 Chat Interactivo con Gemini
- Conversaciones fluidas con el modelo Gemini de Google
- Historial de conversaciones persistente
- Formateo inteligente de respuestas (negritas, código, listas)

### 📁 Gestión de Conversaciones
- Guarda y carga conversaciones automáticamente
- Selección interactiva de conversaciones existentes
- Creación de nuevas conversaciones con nombres personalizados
- Resumen automático de conversaciones largas para optimizar el rendimiento

### 🎯 Soporte Multimodal
- **Documentos PDF**: Analiza y responde preguntas sobre archivos PDF
- **Imágenes**: Procesa y describe imágenes
- **Audio**: Transcribe y analiza archivos de audio

### 🗣️ Síntesis de Voz
- Conversión de texto a voz en español
- Velocidad de reproducción optimizada (1.3x)
- Activación opcional con el flag `-v`

### ✏️ Edición Avanzada
- Integración con nvim para editar entradas largas
- Comando `:e` para abrir el editor
- Soporte para entradas multilínea

## 🛠️ Instalación

### Requisitos Previos
- Python 3.7+
- Biblioteca `custom_gemini` (wrapper para la API de Gemini)
- nvim (para edición de texto)

### Dependencias de Python
```bash
pip install InquirerPy gtts pydub playsound
```

### Configuración Inicial
1. Crea la estructura de directorios:
```bash
mkdir -p ~/.gemcli-py/conversations
mkdir -p ~/.gemcli-py/config
```

2. Configura tu API key de Gemini en el archivo de configuración correspondiente.

## 📖 Uso

### Inicio Básico
```bash
python Main.py
```

### Con Síntesis de Voz
```bash
python Main.py conversation_name -v
```

### Comandos Disponibles
- **Texto normal**: Envía una pregunta directamente a Gemini
- **`:exit`**: Cierra la aplicación
- **`:e`**: Abre nvim para editar una entrada más larga
- **Ctrl+C**: Salida de emergencia

### Referencia de Archivos
Para incluir archivos en tus consultas, usa la siguiente sintaxis:

```
# Para PDFs
pdf:'/ruta/al/archivo.pdf'

# Para imágenes
image:'/ruta/a/la/imagen.jpg'

# Para audio
audio:'/ruta/al/audio.mp3'
```

## 🏗️ Estructura del Proyecto

```
gemcli/
├── Main.py                 # Punto de entrada principal
├── project_code/
│   ├── Init.py            # Inicialización y gestión de conversaciones
│   ├── client/            # Módulos cliente
│   │   ├── GeminiCustom.py     # Integración con Gemini API
│   │   ├── Voice.py            # Síntesis de voz
│   │   ├── CreateQuestion.py   # Creación de preguntas
│   │   ├── ResponseQuestion.py # Procesamiento de respuestas
│   │   └── WriteAuxFile.py     # Edición de archivos
│   └── service/           # Capa de servicios
│       └── ProcessInteraction.py # Procesamiento de interacciones
└── README.md
```

## 🎨 Características de Formato

GemCLI formatea automáticamente las respuestas de Gemini:

- **Texto en negrita**: `**texto**` → texto resaltado en verde
- **Bloques de código**: ` ```código``` ` → sección de código con formato especial
- **Listas**: `* elemento` → viñetas con símbolos `•`

## 📁 Almacenamiento

Las conversaciones se guardan en:
```
~/.gemcli-py/conversations/
```

Los archivos de configuración en:
```
~/.gemcli-py/config/
```

## ⚡ Optimizaciones

- **Gestión de memoria**: Las conversaciones largas (>2MB) se resumen automáticamente
- **Audio optimizado**: La síntesis de voz se acelera para una mejor experiencia
- **Archivos temporales**: Se limpian automáticamente después de cada interacción

## 🤝 Contribuciones

Este proyecto está diseñado para ser extensible. Las áreas principales para contribuciones incluyen:

- Nuevos formatos de archivo multimodal
- Mejoras en la síntesis de voz
- Optimizaciones de rendimiento
- Nuevas características de formato de texto

## 📝 Notas

- El proyecto está configurado para trabajar con rutas específicas del usuario (`/home/daniel/`)
- Requiere configuración inicial de la API de Gemini
- Optimizado para uso en sistemas Unix/Linux