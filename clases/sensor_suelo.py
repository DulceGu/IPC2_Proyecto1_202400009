from listas.lista_enlazada import ListaEnlazada

class SensorSuelo:
    def __init__(self, id_sensor, nombre):
        self.id_sensor = id_sensor
        self.nombre = nombre
        self.frecuencias = ListaEnlazada()  # aqui la vuelvo lista enlasdaza
        