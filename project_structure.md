# 📁 Estructura del Proyecto PNL

Este documento describe la estructura organizacional del repositorio de Procesamiento de Lenguaje Natural.

---

## 🌳 Árbol de Directorios

```
PNL/
│
├── 📂 01 Introducción a PNL/
│   ├── 📓 01_fundamentos_nlp.ipynb
│   ├── 📓 02_historia_evolucion.ipynb
│   ├── 📓 03_aplicaciones_actuales.ipynb
│   ├── 📄 README.md
│   └── 📂 recursos/
│       ├── papers/
│       └── presentaciones/
│
├── 📂 02 Python/
│   ├── 📓 01_estructuras_datos.ipynb
│   ├── 📓 02_librerias_esenciales.ipynb
│   ├── 📓 03_buenas_practicas.ipynb
│   ├── 📓 04_python_para_nlp.ipynb
│   ├── 📄 README.md
│   └── 📂 ejercicios/
│       ├── ejercicio_01.py
│       └── ejercicio_02.py
│
├── 📂 03 De sopa de letras al análisis lingüístico/
│   ├── 📓 01_tokenizacion.ipynb
│   ├── 📓 02_normalizacion.ipynb
│   ├── 📓 03_limpieza_texto.ipynb
│   ├── 📓 04_expresiones_regulares.ipynb
│   ├── 📄 README.md
│   └── 📂 ejemplos/
│       ├── texto_sucio.txt
│       └── texto_limpio.txt
│
├── 📂 04 Vectorización de texto y text mining/
│   ├── 📓 01_bag_of_words.ipynb
│   ├── 📓 02_tfidf.ipynb
│   ├── 📓 03_analisis_frecuencias.ipynb
│   ├── 📓 04_n_gramas.ipynb
│   ├── 📄 README.md
│   └── 📂 datos/
│       └── corpus_ejemplo.txt
│
├── 📂 05 Text Mining/
│   ├── 📓 01_analisis_sentimientos.ipynb
│   ├── 📓 02_clasificacion_textos.ipynb
│   ├── 📓 03_extraccion_informacion.ipynb
│   ├── 📓 04_topic_modeling.ipynb
│   ├── 📄 README.md
│   └── 📂 modelos/
│       ├── clasificador.pkl
│       └── vectorizador.pkl
│
├── 📂 06 Introducción a embeddings/
│   ├── 📓 01_word2vec.ipynb
│   ├── 📓 02_glove.ipynb
│   ├── 📓 03_fasttext.ipynb
│   ├── 📓 04_comparacion_embeddings.ipynb
│   ├── 📄 README.md
│   └── 📂 embeddings/
│       ├── .gitkeep
│       └── README.md (instrucciones de descarga)
│
├── 📂 07 Redes Neuronales/
│   ├── 📓 01_introduccion_rnn.ipynb
│   ├── 📓 02_lstm_gru.ipynb
│   ├── 📓 03_transformers.ipynb
│   ├── 📓 04_bert_gpt.ipynb
│   ├── 📄 README.md
│   └── 📂 arquitecturas/
│       ├── modelo_simple.py
│       └── modelo_avanzado.py
│
├── 📂 08 Laboratorio de desarrollo/
│   ├── 📓 proyecto_01_clasificador.ipynb
│   ├── 📓 proyecto_02_chatbot.ipynb
│   ├── 📓 proyecto_03_resumen_texto.ipynb
│   ├── 📄 README.md
│   └── 📂 proyectos/
│       ├── clasificador/
│       ├── chatbot/
│       └── resumen_automatico/
│
├── 📂 cabrera-vanesa-nlp-integrador/
│   ├── 📓 analisis_exploratorio.ipynb
│   ├── 📓 preprocesamiento.ipynb
│   ├── 📓 modelado.ipynb
│   ├── 📓 evaluacion.ipynb
│   ├── 📄 README.md
│   ├── 📄 informe_final.pdf
│   └── 📂 src/
│       ├── __init__.py
│       ├── preprocess.py
│       ├── models.py
│       ├── utils.py
│       └── visualization.py
│
├── 📂 clase 14 de octubre/
│   ├── 📓 notas_clase.ipynb
│   ├── 📓 ejercicios_clase.ipynb
│   └── 📄 README.md
│
├── 📂 Colab Integrador/
│   ├── 📓 proyecto_integrador_colab.ipynb
│   ├── 📄 README.md
│   └── 📂 datos/
│       └── dataset_integrador.csv
│
├── 📂 Ejercicio a entregar/
│   ├── 📓 ejercicio_evaluable.ipynb
│   ├── 📄 README.md
│   └── 📄 rubrica_evaluacion.md
│
├── 📂 assets/
│   ├── 🖼️ banner.png
│   ├── 🖼️ logo.png
│   └── 📂 images/
│       ├── arquitectura_modelo.png
│       └── resultados_grafica.png
│
├── 📂 docs/
│   ├── 📄 guia_instalacion.md
│   ├── 📄 troubleshooting.md
│   ├── 📄 glosario.md
│   └── 📄 recursos_adicionales.md
│
├── 📂 scripts/
│   ├── 🐍 setup_environment.py
│   ├── 🐍 download_datasets.py
│   ├── 🐍 train_model.py
│   └── 🐍 evaluate_model.py
│
├── 📂 tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_models.py
│   └── test_utils.py
│
├── 📂 utils/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluation.py
│   └── visualization.py
│
├── 📂 .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── publish.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── 📄 .gitignore
├── 📄 .gitattributes
├── 📄 README.md
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 requirements-dev.txt
├── 📄 setup.py
├── 📄 pyproject.toml
├── 📄 CHANGELOG.md
└── 📄 project_structure.md (este archivo)
```

---

## 📖 Descripción de Directorios

### 📚 Módulos de Contenido (01-08)

Cada módulo sigue una estructura similar:

```
[Número] [Nombre del Módulo]/
├── [Número]_[nombre_tema].ipynb    # Notebooks principales
├── README.md                        # Descripción del módulo
└── [carpeta_recursos]/             # Recursos adicionales
    ├── datos/
    ├── modelos/
    ├── ejemplos/
    └── ejercicios/
```

### 🎯 Proyecto Integrador

```
cabrera-vanesa-nlp-integrador/
├── notebooks/                       # Análisis por etapas
├── src/                            # Código fuente
├── data/                           # Datos (no versionados)
├── models/                         # Modelos entrenados
├── results/                        # Resultados y métricas
├── docs/                           # Documentación específica
├── README.md                       # Descripción del proyecto
└── requirements.txt                # Dependencias específicas
```

### 🛠️ Utilidades y Scripts

#### `scripts/`
Scripts ejecutables para tareas comunes:
- **setup_environment.py**: Configuración inicial del entorno
- **download_datasets.py**: Descarga de datasets necesarios
- **train_model.py**: Entrenamiento de modelos
- **evaluate_model.py**: Evaluación de modelos

#### `utils/`
Módulo Python con funciones reutilizables:
- **preprocessing.py**: Funciones de preprocesamiento
- **feature_engineering.py**: Creación de features
- **evaluation.py**: Métricas y evaluación
- **visualization.py**: Funciones de visualización

### 🧪 Tests

```
tests/
├── __init__.py
├── test_preprocessing.py            # Tests de preprocesamiento
├── test_models.py                   # Tests de modelos
├── test_utils.py                    # Tests de utilidades
└── conftest.py                      # Configuración de pytest
```

### 📄 Documentación

```
docs/
├── guia_instalacion.md              # Guía de instalación
├── troubleshooting.md               # Solución de problemas
├── glosario.md                      # Términos técnicos
├── recursos_adicionales.md          # Links y recursos
└── api/                             # Documentación de API
```

### 🎨 Assets

```
assets/
├── banner.png                       # Banner del proyecto
├── logo.png                         # Logo
└── images/                          # Imágenes del proyecto
    ├── screenshots/
    ├── diagrams/
    └── results/
```

---

## 📝 Convenciones de Nombrado

### Archivos Python
```python
# Módulos: snake_case
preprocessing.py
feature_engineering.py

# Clases: PascalCase
class TextPreprocessor:
    pass

# Funciones: snake_case
def clean_text(text):
    pass

# Constantes: UPPER_CASE
MAX_TOKENS = 512
```

### Notebooks
```
[numero]_[nombre_descriptivo].ipynb

Ejemplos:
01_introduccion_nlp.ipynb
02_analisis_sentimientos.ipynb
```

### Carpetas
```
# snake_case o kebab-case
data_raw/
modelos-entrenados/

# Números de módulo con espacio
01 Introducción a PNL/
02 Python/
```

---

## 🔄 Flujo de Trabajo Recomendado

### 1. Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/22823992-sudo/PNL.git
cd PNL

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear nueva rama
git checkout -b feature/nueva-funcionalidad
```

### 2. Trabajo con Notebooks

```bash
# Iniciar Jupyter
jupyter notebook

# O JupyterLab
jupyter lab
```

### 3. Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=utils tests/

# Test específico
pytest tests/test_preprocessing.py
```

### 4. Commit y Push

```bash
# Añadir cambios
git add .

# Commit
git commit -m "Add: nueva funcionalidad de tokenización"

# Push
git push origin feature/nueva-funcionalidad
```

---

## 📦 Gestión de Datos

### Estructura de Datos (No Versionada)

```
data/                                # No subir a Git
├── raw/                            # Datos originales
│   ├── corpus.txt
│   └── dataset.csv
├── processed/                      # Datos procesados
│   ├── corpus_clean.txt
│   └── features.pkl
├── interim/                        # Datos intermedios
│   └── tokens.pkl
└── external/                       # Datos externos
    └── embeddings/
        └── word2vec.bin
```

### Archivos `.gitkeep`

Para mantener la estructura de carpetas vacías:

```bash
# Crear .gitkeep en carpetas vacías
touch data/.gitkeep
touch models/.gitkeep
touch results/.gitkeep
```

---

## 🔐 Archivos Sensibles

### NO versionar:

- ❌ Credenciales y API keys (`.env`, `config/secrets.py`)
- ❌ Modelos grandes (`.h5`, `.pkl`, `.pth`)
- ❌ Datasets grandes (`.csv`, `.json`)
- ❌ Resultados y logs (`results/`, `logs/`)
- ❌ Caché (`.cache/`, `__pycache__/`)

### SÍ versionar:

- ✅ Código fuente (`.py`, `.ipynb`)
- ✅ Configuraciones (`.yaml`, `.json`)
- ✅ Documentación (`.md`)
- ✅ Tests (`test_*.py`)
- ✅ Ejemplos pequeños (`sample_data.csv`)

---

## 🎯 Mejores Prácticas

### 1. Organización de Notebooks

```python
# Estructura recomendada de un notebook

# 1. Título y Descripción
"""
# Título del Notebook
Descripción breve del contenido
Autor: Vanesa Cabrera
Fecha: 2025-11-18
"""

# 2. Imports
import numpy as np
import pandas as pd
# ... más imports

# 3. Configuración
%matplotlib inline
pd.set_option('display.max_columns', None)

# 4. Carga de Datos
# ...

# 5. Análisis Exploratorio
# ...

# 6. Preprocesamiento
# ...

# 7. Modelado
# ...

# 8. Evaluación
# ...

# 9. Conclusiones
# ...
```

### 2. Documentación de Funciones

```python
def procesar_texto(texto: str, lowercase: bool = True) -> str:
    """
    Procesa un texto aplicando transformaciones básicas.
    
    Args:
        texto (str): Texto a procesar
        lowercase (bool): Si convertir a minúsculas
        
    Returns:
        str: Texto procesado
        
    Examples:
        >>> procesar_texto("HOLA Mundo")
        'hola mundo'
    """
    if lowercase:
        texto = texto.lower()
    return texto.strip()
```

### 3. README por Módulo

Cada carpeta de módulo debe tener un `README.md`:

```markdown
# Módulo X: Nombre del Módulo

## Descripción
Breve descripción del contenido

## Contenido
- Notebook 1: Descripción
- Notebook 2: Descripción

## Objetivos de Aprendizaje
- Objetivo 1
- Objetivo 2

## Requisitos
- Prerequisitos

## Recursos Adicionales
- Links útiles
```

---

## 🚀 Próximos Pasos

1. ✅ Crear estructura base de carpetas
2. ✅ Configurar `.gitignore`
3. ✅ Añadir documentación inicial
4. ⬜ Organizar notebooks existentes
5. ⬜ Crear módulo `utils/`
6. ⬜ Añadir tests
7. ⬜ Documentar funciones principales
8. ⬜ Crear ejemplos de uso

---

## 📞 Contacto

Para sugerencias sobre la estructura del proyecto:

- 🐛 Reportar problema: [Issues](https://github.com/22823992-sudo/PNL/issues)
- 💡 Sugerir mejora: [Discussions](https://github.com/22823992-sudo/PNL/discussions)

---

<div align="center">

**📁 Mantén tu proyecto organizado = 🚀 Proyecto exitoso**

</div>