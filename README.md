# Bible Text Mining

## Sistema de análisis de un corpus bíblico mediante técnicas de Procesamiento de Lenguaje Natural

Este proyecto implementa un sistema de análisis textual sobre la **Biblia Reina-Valera 1960** utilizando técnicas clásicas de Procesamiento de Lenguaje Natural (Natural Language Processing, NLP).

El sistema permite realizar el preprocesamiento del corpus, representar documentos mediante TF-IDF, recuperar información utilizando similitud del coseno, clasificar versículos mediante Naive Bayes, generar texto utilizando modelos N-Gram y realizar un análisis de sentimiento. Además, genera distintas visualizaciones que facilitan el análisis del corpus.

El desarrollo fue realizado en **Python**, utilizando un enfoque de **Programación Orientada a Objetos**, con el objetivo de obtener una solución modular, reutilizable y de fácil mantenimiento.

---

# Funcionalidades

El sistema implementa las siguientes funcionalidades:

- Preprocesamiento del corpus bíblico.
- Construcción manual de la representación TF-IDF.
- Implementación manual de la similitud del coseno.
- Motor de búsqueda semántico.
- Clasificación automática mediante Naive Bayes.
- Generación de texto utilizando modelos Unigrama, Bigrama, Trigrama y Cuatrigrama.
- Análisis de sentimiento.
- Generación automática de visualizaciones.

---

# Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Python | Lenguaje principal |
| Pandas | Manipulación de datos |
| NumPy | Cálculo numérico |
| Matplotlib | Visualización |
| Scikit-Learn | Clasificación y reducción de dimensionalidad (PCA) |
| TextBlob | Análisis de sentimiento |

---

# Arquitectura del proyecto

La estructura general del proyecto es la siguiente:

```text
biblical-text-mining/
│
├── data/
│   └── bible.csv
│
├── src/
│   ├── buscador.py
│   ├── experimentos.py
│   ├── ngram.py
│   ├── preprocesamiento.py
│   ├── similitud.py
│   ├── tfidf.py
│   └── utils.py
│
├── main.py
├── README.md
├── Informe_Taller2.pdf
├── diagrama_de_clases.png
├── heatmap_libros.png
├── histograma_versiculos.png
├── pca_versiculos.png
└── sentimiento_libros.png
```

El repositorio incluye además la siguiente documentación y archivos generados:

- **Informe_Taller2.pdf**: informe técnico con el desarrollo completo del laboratorio.
- **diagrama_de_clases.png**: diagrama UML de la arquitectura implementada.
- **heatmap_libros.png**: mapa de calor de similitud entre libros.
- **histograma_versiculos.png**: distribución de longitud de los versículos.
- **pca_versiculos.png**: proyección bidimensional mediante PCA.
- **sentimiento_libros.png**: sentimiento promedio por libro.

---

# Requisitos

Para ejecutar el proyecto se requiere:

- Python 3.10 o superior.

Instalar las siguientes bibliotecas:

- pandas
- numpy
- matplotlib
- scikit-learn
- textblob

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/carlosbuguenocortes/bible-text-mining.git
```

Ingresar al directorio del proyecto:

```bash
cd bible-text-mining
```

Instalar las dependencias:

```bash
pip install pandas numpy matplotlib scikit-learn textblob
```

---

# Ejecución

Ejecutar el programa principal mediante:

```bash
python main.py
```

---

# Funcionamiento

Al ejecutar el programa, el sistema realiza automáticamente las siguientes etapas:

1. Carga el corpus bíblico.
2. Realiza el preprocesamiento del texto.
3. Construye la representación TF-IDF.
4. Calcula la similitud entre documentos.
5. Ejecuta el motor de búsqueda semántico.
6. Entrena y evalúa el clasificador Naive Bayes.
7. Genera texto utilizando modelos N-Gram.
8. Realiza el análisis de sentimiento.
9. Genera las visualizaciones del corpus.

Durante la ejecución se generan los siguientes archivos:

- `heatmap_libros.png`
- `histograma_versiculos.png`
- `pca_versiculos.png`
- `sentimiento_libros.png`

---

# Integrantes

- Carlos Bugueño
- Constantino Bekios
- Vicente Moyano
