# 📖 Bible Text Mining - Minería de Texto en la Biblia

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![NLP](https://img.shields.io/badge/NLP-Text%20Mining-orange.svg)

**Revelando patrones y conexiones en la Biblia con minería de texto en Python**

Aplicación de técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **minería de texto** a la Biblia Reina-Valera 1960 en español para descubrir patrones lingüísticos, relaciones semánticas entre libros bíblicos y analizar frecuencias de términos.

---

## 📊 Características del Proyecto

- 🔍 **Análisis de frecuencias** de palabras y términos bíblicos
- 📈 **Comparación entre libros** de la Biblia
- 🕸️ **Análisis de co-ocurrencias** entre palabras
- 🌐 **Matriz de similitud semántica** entre libros
- ☁️ **Nube de palabras** con los términos más frecuentes
- 📊 **Visualizaciones** con matplotlib, seaborn y wordcloud
- 📁 **Exportación de resultados** en múltiples formatos

---

##  Estructura del Repositorio
```text
bible-text-mining/
├── data/ # Datos textuales de la Biblia
│ ├── biblia.txt # Texto completo Reina-Valera 1960
│ └── books/ # Libros individuales (opcional)
├── outputs/ # Resultados generados
│ ├── figures/ # Gráficos y visualizaciones
│ └── statistics/ # Tablas y estadísticas
├── bible_processing.py # Módulo de procesamiento de texto
├── bible_analysis.ipynb # Notebook Jupyter con análisis completo
├── requirements.txt # Dependencias del proyecto
├── setup.sh # Script de configuración automática
└── README.md # Este archivo
```

---

##  Requisitos del Sistema

### Requisitos Mínimos
- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **4 GB de RAM** (recomendado 8 GB para análisis completos)
- **2 GB de espacio en disco**

### Dependencias Principales
```text
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
wordcloud==1.9.3
scikit-learn==1.3.0
nltk==3.8.1
jupyter==1.0.0
notebook==7.0.3
```
---

## 💻 Instalación y Ejecución

```bash
#### Paso 1: Clonar el repositorio
# Clonar el repositorio
git clone https://github.com/carlosbuguenocortes/bible-text-mining.git
cd bible-text-mining
```


Paso 2: Crear y activar entorno virtual
```bash
# Instalar python3-venv si no está instalado
sudo apt update
sudo apt install python3-venv python3-pip -y

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Verificar activación (debe mostrar la ruta del venv)
which python
```
Paso 3: Script de instalación automática
```bash
# Dar permisos de ejecución
chmod +x setup.sh

# Ejecutar script de configuración
./setup.sh
```
Paso 4: Usar screen para sesiones persistentes
```bash
# Crear una sesión screen (para que el proceso siga aunque se corte la conexión)
screen -S bible-mining

# Dentro de screen, activar el entorno virtual
source venv/bin/activate

# Ejecutar el análisis
python bible_processing.py

# Para desconectarse de screen sin detener el proceso:
# Presionar Ctrl+A, luego D

# Para reconectarse más tarde:
screen -r bible-mining
```
Paso 5: Ejecutar Jupyter Notebook en el servidor
```bash
# Iniciar Jupyter en el servidor (sin navegador)
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0

# En tu máquina local, crear túnel SSH para acceder
# Desde terminal local:
ssh -N -L 8888:localhost:8888 usuario@direccion_ip_servidor

# Luego abrir en el navegador local:
# http://localhost:8888
```

 Uso del Notebook Jupyter
1. El notebook bible_analysis.ipynb contiene las siguientes secciones:
2. Carga de datos: Importación y lectura del texto bíblico
3. Preprocesamiento: Limpieza, tokenización y eliminación de stopwords
4. Análisis de frecuencias: Palabras más comunes por libro
5. Análisis de co-ocurrencias: Relaciones entre términos
6. Similitud entre libros: Matriz de similitud coseno
7. Visualizaciones: Nubes de palabras, heatmaps, gráficos de barras
