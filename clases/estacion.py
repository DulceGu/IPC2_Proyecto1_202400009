from listas.lista_enlazada import ListaEnlazada

class Estacion:
    def __init__(self, id_estacion, nombre):
        self.id_estacion = id_estacion
        self.nombre = nombre
        self.sensores_suelo = ListaEnlazada() #posiblemente lo borre, saber que sensores se miden
        self.sensores_plantas = ListaEnlazada() #posiblemente lo borre
