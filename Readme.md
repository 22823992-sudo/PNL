import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar datos
textos = ["Ejemplo de texto para NLP", "Procesamiento de lenguaje natural"]

# Vectorizar
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(textos)

print(X.toarray())