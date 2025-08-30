from listas.lista_enlazada import ListaEnlazada

class SensorPlantas:
    def __init__(self, id_sensor, nombre):
        self.id_sensor = id_sensor
        self.nombre = nombre
        self.frecuencias = ListaEnlazada()  # lista para las frecuencias (asociadas a estaciones)
