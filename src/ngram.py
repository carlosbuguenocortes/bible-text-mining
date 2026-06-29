import random

class Bigrama:

    def __init__(self, documentos):
        self.modelo = {}

        for doc in documentos:
            for i in range(len(doc)-1):
                w1, w2 = doc[i], doc[i+1]

                if w1 not in self.modelo:
                    self.modelo[w1] = []

                self.modelo[w1].append(w2)

    def generar(self, inicio=None, longitud=15):
        import random

        # si no hay inicio o no existe, elegir uno válido
        if inicio is None or inicio not in self.modelo:
            inicio = random.choice(list(self.modelo.keys()))

        palabra = inicio
        resultado = [palabra]

        for _ in range(longitud):
            if palabra not in self.modelo:
                break

            palabra = random.choice(self.modelo[palabra])
            resultado.append(palabra)

        return " ".join(resultado)

#creo clase Trigrama para generar texto basado en trigramas para lograr mas coherencia.
class Trigrama:

    def __init__(self, documentos):
        self.modelo = {}

        for doc in documentos:
            for i in range(len(doc)-2):
                w1, w2, w3 = doc[i], doc[i+1], doc[i+2]

                clave = (w1, w2)

                if clave not in self.modelo:
                    self.modelo[clave] = []

                self.modelo[clave].append(w3)

    def generar(self, inicio=None, longitud=15):

        # elegir inicio si no se da o no existe
        if inicio is None:
            inicio = random.choice(list(self.modelo.keys()))

        else:
            partes = inicio.split()
            if len(partes) < 2 or (partes[0], partes[1]) not in self.modelo:
                inicio = random.choice(list(self.modelo.keys()))
            else:
                inicio = (partes[0], partes[1])

        resultado = [inicio[0], inicio[1]]

        for _ in range(longitud):
            clave = (resultado[-2], resultado[-1])

            if clave not in self.modelo:
                break

            siguiente = random.choice(self.modelo[clave])
            resultado.append(siguiente)

        return " ".join(resultado)
    
#solo creo para lograr mas coherencia en el texto generado.
#si me sobreajusta no lo uso, pero si me da coherencia lo uso.

class Cuatrigrama:

    def __init__(self, documentos):
        self.modelo = {}

        for doc in documentos:
            for i in range(len(doc)-3):
                w1, w2, w3, w4 = doc[i], doc[i+1], doc[i+2], doc[i+3]

                clave = (w1, w2, w3)

                if clave not in self.modelo:
                    self.modelo[clave] = []

                self.modelo[clave].append(w4)

    def generar(self, inicio=None, longitud=15):

        if inicio is None:
            inicio = random.choice(list(self.modelo.keys()))
        else:
            partes = inicio.split()

            if len(partes) < 3 or tuple(partes[:3]) not in self.modelo:
                inicio = random.choice(list(self.modelo.keys()))
            else:
                inicio = tuple(partes[:3])

        resultado = list(inicio)

        for _ in range(longitud):
            clave = tuple(resultado[-3:])

            if clave not in self.modelo:
                break

            siguiente = random.choice(self.modelo[clave])
            resultado.append(siguiente)

        return " ".join(resultado)