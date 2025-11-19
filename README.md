# 🧠 Natural Language Processing - PNL

![Banner](./assets/banner.png)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

**Repositorio de Procesamiento de Lenguaje Natural**

*Por Vanesa Cabrera*

</div>

---

## 📋 Sobre este Repositorio

Este repositorio contiene material completo sobre **Procesamiento de Lenguaje Natural (PNL/NLP)**, incluyendo fundamentos teóricos, implementaciones prácticas, ejercicios y proyectos integradores.

### ✨ Contenido

* 📖 Material teórico estructurado por módulos
* 💻 Notebooks interactivos con ejemplos prácticos
* 🔬 Proyectos de laboratorio y ejercicios resueltos
* 🧪 Implementaciones de algoritmos de NLP
* 🎓 Proyecto integrador completo
* 📁 Recursos para RAG, APIs y LLMs

---

## 📁 Estructura del Proyecto

```
PNL/
├── 01 Introducción a PNL/
├── 02 Python/
├── 03 De sopa de letras al análisis lingüístico/
├── 04 Vectorización de texto y text mining/
├── 05 Text Mining/
├── 06 Introducción a embeddings/
├── 07 Redes Neuronales/
├── 08 Laboratorio de desarrollo/
├── 09 Transfer Learning/
├── 10 LLMs/
├── 11 APIs - RAG/
├── Rag - TP Final/
├── Ejercicio a entregar/
├── cabrera-vanesa-nlp-integrador/
├── Colab Integrador/
├── assets/
├── banner.html
├── project_structure.md
├── README.md
└── Requirements.txt
```

📄 Ver **project_structure.md** para más detalles.

---

## 🚀 Instalación

### Requisitos Previos

* Python 3.8 o superior
* pip
* Git

### Instalación

```bash
git clone https://github.com/22823992-sudo/PNL.git
cd PNL
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📚 Módulos

### 1️⃣ Introducción a PNL

Fundamentos y aplicaciones del procesamiento de lenguaje natural.

### 2️⃣ Python para NLP

Conceptos de Python esenciales para trabajar con texto.

### 3️⃣ Procesamiento de Texto

Tokenización, normalización y limpieza.

### 4️⃣ Vectorización y Text Mining

TF-IDF, BoW y análisis de frecuencias.

### 5️⃣ Text Mining Avanzado

Clasificación, análisis de sentimientos y extracción de información.

### 6️⃣ Embeddings

Modelos Word2Vec, GloVe y representaciones vectoriales.

### 7️⃣ Redes Neuronales

RNNs, LSTMs y arquitecturas modernas.

### 8️⃣ Laboratorio de Desarrollo

Prácticas, experimentos y mini‑proyectos.

### 9️⃣ Transfer Learning

Modelos preentrenados aplicados a NLP.

### 🔟 LLMs

Uso de modelos grandes de lenguaje, finetuning y evaluación.

### 1️⃣1️⃣ APIs y RAG

Construcción de pipelines RAG, indexación y orquestación.

### 📦 Rag - TP Final

Trabajo práctico final con arquitectura RAG.

### 📝 Ejercicio a entregar

Material requerido para la entrega final.

### 🧩 Proyecto Integrador

Implementaciones finales dentro de `cabrera-vanesa-nlp-integrador`.

---

## 💡 Uso

### Ejecutar Notebooks

```bash
jupyter notebook
```

O utilizar Google Colab cargando los notebooks desde GitHub.

### Ejemplo Rápido

```python
from sklearn.feature_extraction.text import TfidfVectorizer

textos = ["Procesamiento de lenguaje natural", "Aprendiendo NLP"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(textos)
print(X.toarray())
```

---

## 🛠️ Tecnologías

* Python
* NLTK
* spaCy
* scikit-learn
* TensorFlow / PyTorch
* Pandas / NumPy
* Jupyter Notebooks

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Consulta **CONTRIBUTING.md** para detalles.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

## 📫 Contacto

**Vanesa Cabrera**

* GitHub: @22823992-sudo
* Repositorio: PNL

<div align="center">

**⭐ Si este proyecto te resultó útil, considera darle una estrella ⭐**

Made with ❤️ by Vanesa Cabrera

</div>
