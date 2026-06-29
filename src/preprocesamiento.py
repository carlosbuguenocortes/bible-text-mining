import re

STOPWORDS = {
    "el","la","los","las","de","y","a","en","que","un","una",
    "por","con","no","se","su","al","lo","como","más","pero"
}

class Preprocesador:

    def __init__(self, texto):
        self.texto = texto

    def limpiar(self):
        texto = self.texto.lower()
        texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)
        return texto

    def tokenizar(self):
        return self.limpiar().split()

    def eliminar_stopwords(self, tokens):
        return [t for t in tokens if t not in STOPWORDS]

    def procesar(self):
        tokens = self.tokenizar()
        tokens = self.eliminar_stopwords(tokens)
        return tokens