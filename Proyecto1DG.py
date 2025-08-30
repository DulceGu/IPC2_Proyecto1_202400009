# Archivo: Proyecto1DG.py
# Proyecto: Agricultura de Precisión - IPC2
# Estudiante: Dulce Maria Esperanza Gutierrez Caceres
# Carnet: 202400009
# Proyecto1DG.py
# Archivo principal del proyecto

from servicios.manejador_xml import cargar_campos_desde_xml
from servicios.procesador import procesar_campos
from servicios.generador_salida import generar_xml_salida
from servicios.graficador import generar_grafica
import copy

# mis variables globales
campos_originales = []  # para gráficas originales 
campos = []             # para procesar y generar salida

class Menu:
    def __init__(self):
        self.opcion = 0

    def mostrar_menu(self):
        print("\n" + "~"*50)
        print("     Bienvenido..Menu:    ")
        print("~"*50)
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salida")
        print("-"*50)

    def pedir_opcion(self):
        try:
            self.opcion = int(input("Seleccione una opción (1-6): "))
            return self.opcion
        except ValueError:
            print("Ingrese un número válido")
            return -1

    def ejecutar_opcion(self):
        global campos  # esto es necesario para acceder a la variable global

        if self.opcion == 1:
            print("Opción 1: Cargar Archivo")
            ruta = input("Ingrese la ruta del archivo: ")
            nombre = input("Ingrese el nombre del archivo: ")
            global campos_originales, campos
            campos_originales = cargar_campos_desde_xml(ruta + "/" + nombre)
            campos = copy.deepcopy(campos_originales)  # copia profunda para procesar
            print("Datos cargados. Use la opción 2 para procesar.")
        
        elif self.opcion == 2:
            print("Opción 2: Procesar Archivo")
            if not campos_originales:
                print("No hay datos cargados.")
            else:
                campos = procesar_campos(copy.deepcopy(campos_originales))  # pp.rocesa copia profunda
                print("Procesamiento completado.")

        elif self.opcion == 3:
            print("Opción 3: Escribir Archivo de Salida")
            if not campos:
                print("No hay datos procesados.")
            else:
                ruta = input("Ingrese la ruta para guardar: ")
                nombre = input("Ingrese el nombre del archivo de salida: ")
                generar_xml_salida(campos, ruta, nombre)

        elif self.opcion == 4:
            print("Opción 4: Mostrar datos del estudiante")
            print("\n" + "-"*40)
            print("Nombre: Dulce Maria Esperanza Gutierrez Caceres")
            print("Carné: 202400009")
            print("Curso: Introducción a la Programación y Computación 2")
            print("Carrera: Ingeniería en Ciencias y Sistemas")
            print("Semestre: 4to Semestre")
            print("Sección: C")
            print("GitHub: https://github.com/DulceGu/IPC2_Proyecto1_202400009.git")
            print("-"*40)

        elif self.opcion == 5:
            print("Opción 5: Generar gráfica")
            from servicios.graficador import generar_grafica
            generar_grafica(campos_originales, campos)

        elif self.opcion == 6:
            print("Saliendo del sistema Asdiositooo  =D")
            return False

        else:
            print("Error. Intente de nuevo.")

        input("Presione Enter para continuar...")
        return True

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = self.pedir_opcion()
            if opcion == -1:
                continue
            continuar = self.ejecutar_opcion()
            if not continuar:
                break


# funcionar el programa
if __name__ == "__main__":
    menu = Menu()
    menu.iniciar()