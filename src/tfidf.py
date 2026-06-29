import math

class TFIDF:

    def __init__(self, documentos):
        self.docs = documentos
        self.vocabulario = list(set(p for doc in documentos for p in doc))
        self.idf = {}

    def calcular_idf(self):
        print("Calculando IDF...")
        N = len(self.docs)

        for palabra in self.vocabulario:
            df = sum(1 for doc in self.docs if palabra in doc)
            self.idf[palabra] = math.log(N / (df + 1))

    def calcular_tf(self, doc):
        tf = {}

        for palabra in doc:
            tf[palabra] = doc.count(palabra) / len(doc)

        return tf

    def transformar(self):
        self.calcular_idf()

        vectores = []

        for doc in self.docs:
            tf = self.calcular_tf(doc)
            vector = [tf.get(p, 0) * self.idf[p] for p in self.vocabulario]
            vectores.append(vector)

        return vectores

    def transformar_query(self, tokens):
        tf = {}

        for palabra in tokens:
            tf[palabra] = tokens.count(palabra) / len(tokens)

        vector = [tf.get(p, 0) * self.idf.get(p, 0) for p in self.vocabulario]

        return vector
