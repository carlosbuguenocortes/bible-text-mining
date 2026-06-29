from src.preprocesamiento import Preprocesador
from src.similitud import similitud_coseno

def buscar(frase, modelo_tfidf, vectores, df):

    # procesar frase
    tokens = Preprocesador(frase).procesar()

    # convertir a vector
    vector_query = modelo_tfidf.transformar_query(tokens)

    # calcular similitudes
    resultados = []

    for i, v in enumerate(vectores):
        sim = similitud_coseno(vector_query, v)
        resultados.append((i, sim))

    # ordenar por similitud
    resultados.sort(key=lambda x: x[1], reverse=True)

    # obtener top 5
    top = resultados[:5]

    
    return [(df.iloc[i]["book"], df.iloc[i]["chapter"], df.iloc[i]["verse"],
         df.iloc[i]["text"], sim) for i, sim in top]

