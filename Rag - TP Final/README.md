#  Consultor Psicológico Online — Sistema RAG

Sistema de **Retrieval-Augmented Generation (RAG)** diseñado para responder preguntas psicológicas consultando múltiples manuales, libros y documentos digitalizados.

Desarrollado como **Trabajo Integrador Nº2**  
Materia: *Procesamiento del Habla e Introducción a LLMs*  
Institución: *IFTS 24*  
Año: **2025**

---

##  Descripción

Este sistema permite consultar una gran cantidad de información psicológica almacenada en varios documentos PDF, los cuales se procesan, dividen en fragmentos, se embeben y almacenan en una base de datos vectorial.

Mediante una interfaz simple, el usuario puede hacer preguntas y obtener respuestas basadas **exclusivamente en el contenido del corpus cargado**.

---

##  Demo

🔗 *(Agregar link cuando el deploy esté disponible)*

---

##  Problema que Resuelve

- Permite gestionar grandes cantidades de información psicológica.
- Facilita la consulta rápida y precisa.
- Genera respuestas basadas en fuentes reales, no inventadas.
- Reduce la dependencia de búsquedas manuales en textos extensos.

---

#  Arquitectura del Sistema

##  **Pipeline RAG**

| Etapa            | Descripción |
|------------------|-------------|
| **Ingesta**      | Carga de PDFs mediante `PyMuPDFLoader` |
| **Chunking**     | `chunk_size=1500` con `chunk_overlap=150` (mejores resultados obtenidos) |
| **Embeddings**   | `sentence-transformers/all-MiniLM-L12-v2` (rápido y eficiente) |
| **Vector DB**    | ChromaDB persistente |
| **Retrieval**    | `similarity_search(query, k=3)` |
| **Generación**   | Modelo **Gemini 2.5 Flash** |
| **Interfaz**     | Streamlit |

---

## 🔁 Diagrama de Flujo

 *(Agregar imagen cuando la tengas)*  
Ejemplo:


## PDFs → Chunking → Embeddings → ChromaDB → Consulta → Retrieval → Gemini → Respuesta

#  Stack Tecnológico

###  LLM
- **Gemini** (Google)

###  Embeddings
- **HuggingFace Sentence Transformers**

###  Base Vectorial
- **ChromaDB**

###  Orquestación
- **LangChain**

###  Interfaz
- **Streamlit**

###  Deployment
- **Streamlit Cloud**

###  Otras librerías
- `streamlit`
- `python-dotenv`
- `langchain`
- `langchain-community`
- `chromadb`
- `sentence-transformers`
- `google-genai`
- `langchain_huggingface`

---

#  Corpus de Documentos

- **Dominio:** Psicología  
- **Cantidad:** 10 PDFs  
- **Fuente:** Libros digitales / manuales online  
- **Formato:** PDF  
- **Idioma:** Español  

---

#  Instalación y Uso Local

##  Prerrequisitos
- Python **3.9+**
- API Key de **Gemini**

---

##  Pasos de Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/HugoDaniel1022/rag_v1.git
cd rag_v1

## Crear entorno virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
GEMINI_API_KEY=tu_api_key

# Procesar documentos
python indexacion.py

# Ejecutar la aplicación
streamlit run app.py

#Estructura del proyecto
├── app.py                  # Aplicación Streamlit principal
├── indexacion.py           # Proceso de chunking y generación de embeddings
├── agregar_docs.py         # Funciones auxiliares
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Este archivo
├── .env                    # Configuración local
├── documentos/             # PDFs fuente
│   └── *.pdf
├── chroma_db/              # Base vectorial generada
└── .gitignore              # Exclusiones de Git

# Ejemplos de Consultas

“¿Qué es la educación?”

“¿En base a qué dimensiones se define el nivel de desorden del consultante en DBT?”

“¿Cuáles son las etapas del trastorno DBT?”

“¿Qué es el duelo?”

“¿En qué consiste el tratamiento para abordar el duelo?”

# Decisiones de Diseño
🟣 ¿Por qué Gemini?

Más rápido y eficiente durante las pruebas.

Menor costo en consultas.

Buena comprensión del idioma español.

🟣 ¿Por qué chunk_size=1500 y overlap=150?

Mejor equilibrio entre contexto útil y carga computacional.

Resultados más precisos en recuperación.

🟣 ¿Por qué top-k = 3?

Buen compromiso entre precisión y velocidad.

Devuelve contexto suficiente sin sobrecargar el prompt.

🟣 ¿Por qué Streamlit Cloud?

Fácil de deployar

Familiaridad con la herramienta

Hosting gratuito

# 👥 Autores

Vanesa Cabrera
Hugo D. Peña

🏫 Información Académica

Trabajo Integrador Nº2
Materia: Procesamiento del Habla e Introducción a LLMs
Institución: IFTS 24 – Tecnicatura Superior en Ciencia de Datos e IA
Profesor: Matías Barreto
Año: 2025

# Licencia

Este proyecto se distribuye bajo la licencia MIT.

