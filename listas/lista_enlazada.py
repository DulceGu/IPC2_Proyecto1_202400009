from clases.nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._size = 0

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._size += 1

    def recorrer(self):
        actual = self.primero
        while actual:
            yield actual.valor
            actual = actual.siguiente

    def __iter__(self):
        return self.recorrer()

    def __len__(self):
        return self._size