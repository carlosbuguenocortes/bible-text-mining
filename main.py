# =============================
# 0. IMPORTAR LIBRERÍAS
# =============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.preprocesamiento import Preprocesador
from src.tfidf import TFIDF
from src.buscador import buscar
from src.ngram import Bigrama, Trigrama, Cuatrigrama
from src.experimentos import grafico_longitud, heatmap_libros

# =============================
# 1. CARGAR DATASET
# =============================
filas = []

with open("data/bible.csv", encoding="latin-1") as f:
    lineas = f.readlines()

for linea in lineas[2:]:
    partes = linea.strip().split(",", 5)
    if len(partes) == 6:
        filas.append(partes)

df = pd.DataFrame(filas, columns=[
    "id","book","chapter","verse","subverse","text"
])

df = df[df["id"] != '"Verse ID"']

# =============================
# 2. LIMPIEZA
# =============================
df["book"] = df["book"].str.encode("latin-1").str.decode("utf-8")
df["text"] = df["text"].str.encode("latin-1").str.decode("utf-8")

# =============================
# 3. TESTAMENTO
# =============================
nuevo_testamento = {
    "Mateo","Marcos","Lucas","Juan","Hechos",
    "Romanos","1 Corintios","2 Corintios","Gálatas","Efesios",
    "Filipenses","Colosenses","1 Tesalonicenses","2 Tesalonicenses",
    "1 Timoteo","2 Timoteo","Tito","Filemón",
    "Hebreos","Santiago","1 Pedro","2 Pedro",
    "1 Juan","2 Juan","3 Juan","Judas","Apocalipsis"
}

def detectar_testamento(libro):
    return "Nuevo" if libro.strip() in nuevo_testamento else "Antiguo"

df["testament"] = df["book"].apply(detectar_testamento)

# =============================
# 4. PREPROCESAMIENTO
# =============================
df["tokens"] = df["text"].apply(
    lambda x: Preprocesador(x).procesar()
)

print("\nTamaño dataset completo:")
print(df.shape)

# =============================
# 5. SELECCIÓN DATASET
# =============================

# OPCIÓN 1: dataset completo
df_trabajo = df.copy()

# OPCIÓN 2: dataset mediano (descomentar si quieres rapidez)
# df_trabajo = df.sample(10000, random_state=42)

print("\nTamaño dataset utilizado:")
print(df_trabajo.shape)

# =============================
# 6. VISUALIZACIONES
# =============================
print("\nGenerando visualizaciones...")
grafico_longitud(df_trabajo)
heatmap_libros(df_trabajo)

# =============================
# 7. TF-IDF
# =============================
print("\nCalculando TF-IDF...")
modelo_tfidf = TFIDF(df_trabajo["tokens"].tolist())
vectores = modelo_tfidf.transformar()

print("\nCantidad de vectores:")
print(len(vectores))

# =============================
# 8. PCA
# =============================
from sklearn.decomposition import PCA

print("\nAplicando PCA...")
pca = PCA(n_components=2)
reducido = pca.fit_transform(vectores)

colores = df_trabajo["testament"].map({
    "Antiguo": "blue",
    "Nuevo": "red"
})

plt.scatter(reducido[:,0], reducido[:,1], c=colores)
plt.title("PCA de versículos")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.show()

# =============================
# 9. BUSCADOR
# =============================
print("\nBuscando contexto semántico...")

consulta = "Dios creó la tierra"

resultado = buscar(consulta, modelo_tfidf, vectores, df_trabajo)

print("\nResultados de búsqueda:")
print(resultado)

# =============================
# 10. CLASIFICADOR
# =============================
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

print("\nEntrenando clasificador...")

X_train, X_test, y_train, y_test = train_test_split(
    vectores, df_trabajo["book"], test_size=0.2
)

modelo = MultinomialNB()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("\nAccuracy del clasificador:")
print(accuracy_score(y_test, y_pred))

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# =============================
# 11. N-GRAMAS
# =============================
print("\nGenerando texto con n-gramas...")

modelo_bigram = Bigrama(df_trabajo["tokens"].tolist())
print("\nBigram:")
print(modelo_bigram.generar())

modelo_trigram = Trigrama(df_trabajo["tokens"].tolist())
print("\nTrigram:")
print(modelo_trigram.generar("dios dijo"))

modelo_4gram = Cuatrigrama(df_trabajo["tokens"].tolist())
print("\nCuatrigram:")
print(modelo_4gram.generar())

# =============================
# 12. SENTIMIENTO
# =============================
from textblob import TextBlob

print("\nCalculando sentimiento...")

df_sent = df_trabajo.copy()

df_sent["sentimiento"] = df_sent["text"].apply(
    lambda x: TextBlob(x).sentiment.polarity
)

sentimiento_libro = df_sent.groupby("book")["sentimiento"].mean()

sentimiento_libro.plot(kind="bar", figsize=(12,5))
plt.title("Sentimiento promedio por libro")
plt.ylabel("Sentimiento")
plt.xticks(rotation=90)
plt.show()
