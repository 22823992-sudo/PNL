# 📚 Sistema RAG con Gemini + Chroma + Streamlit

Este proyecto implementa un sistema **RAG (Retrieval-Augmented Generation)** utilizando:

- **Google Gemini 2.5 Flash** como modelo generativo
- **ChromaDB** como base de datos vectorial persistente
- **Sentence Transformers (HuggingFace)** para generar embeddings
- **Streamlit** como interfaz web
- **PDFs locales** como fuente de conocimiento

El objetivo es permitir al usuario realizar preguntas y obtener respuestas basadas **exclusivamente en la información contenida en los documentos cargados**.

---

## 🚀 Funcionalidades

### 🔎 Recuperación Semántica
El sistema utiliza embeddings + Chroma para encontrar los fragmentos más relevantes en los documentos.

### 🧠 Generación con Gemini 2.5 Flash
El contexto recuperado se envía a Gemini junto con la pregunta del usuario.

### 💬 Interfaz web intuitiva
Streamlit permite:
- Ingresar preguntas
- Ver respuestas generadas
- Mostrar el contexto utilizado

### ⚡ Carga optimizada
Uso de:
```python
@st.cache_resource
