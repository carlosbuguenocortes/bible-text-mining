import os
import matplotlib
import matplotlib.pyplot as plt

EN_SERVER = os.environ.get("DISPLAY", "") == ""

if EN_SERVER:
    matplotlib.use("Agg")

def mostrar_o_guardar(nombre_archivo):
    if EN_SERVER:
        plt.savefig(nombre_archivo)
        plt.close()
    else:
        plt.show()
        