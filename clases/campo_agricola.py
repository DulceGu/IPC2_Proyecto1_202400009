from listas.lista_enlazada import ListaEnlazada

class CampoAgricola:
    def __init__(self, id_campo, nombre):
        self.id_campo = id_campo
        self.nombre = nombre
        self.estaciones = ListaEnlazada()
        self.sensores_suelo = ListaEnlazada()
        self.sensores_plantas = ListaEnlazada()