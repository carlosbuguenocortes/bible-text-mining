import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.similitud import similitud_coseno
from src.tfidf import TFIDF

from main import mostrar_o_guardar

def grafico_longitud(df):
    df["longitud"] = df["tokens"].apply(len)

    plt.hist(df["longitud"], bins=50)
    plt.title("Distribución de longitud de versículos")
    plt.xlabel("Cantidad de palabras")
    plt.ylabel("Frecuencia")
    mostrar_o_guardar("histograma_versiculos.png")


def heatmap_libros(df):
    df_heatmap = df.groupby("book").head(50)

    modelo = TFIDF(df_heatmap["tokens"].tolist())
    vectores = modelo.transformar()

    libros = df_heatmap["book"].unique()

    vectores_por_libro = {}

    for libro in libros:
        vects = [
            vectores[i]
            for i in range(len(vectores))
            if df_heatmap.iloc[i]["book"] == libro
        ]

        if len(vects) > 0:
            vectores_por_libro[libro] = np.mean(vects, axis=0)

    n = len(libros)
    matriz = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            matriz[i][j] = similitud_coseno(
                vectores_por_libro[libros[i]],
                vectores_por_libro[libros[j]]
            )

    plt.figure(figsize=(12,10))
    sns.heatmap(matriz, xticklabels=libros, yticklabels=libros, cmap="coolwarm")
    plt.title("Heatmap de similitud entre libros")
    plt.xticks(rotation=90)
    mostrar_o_guardar("heatmap_libros.png")