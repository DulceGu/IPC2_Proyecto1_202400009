# Archivo: Proyecto1DG.py
# Proyecto: Agricultura de Precisión - IPC2
# Estudiante: Dulce Maria Esperanza Gutierrez Caceres
# Carnet: 202400009

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
            print("ingrese un número vAlido")
            return -1

    def ejecutar_opcion(self):
        if self.opcion == 1:
            print("Opción 1: Cargar Archivo")
            # Logica mas ad elante
            input("Presione Enter para continuar...")

        elif self.opcion == 2:
            print("Opción 2: Procesar Archivo")
            #Logica
            input("Presione Enter para continuar...")

        elif self.opcion == 3:
            print("Opción 3: Escribir Archivo de Salida")
            #Lgica
            input("Presione Enter para continuar...")

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
            input("Presione Enter para continuar...")

        elif self.opcion == 5:
            print("Opción 5: Generar gráfica")
            #Logica
            input("Presione Enter para continuar...")

        elif self.opcion == 6:
            print("Saliendo del sistema Asdiositooo  =D")
            return False  # Para salir del bucle

        else:
            print("Error Intente de nuevo")
            input("Presione Enter para continuar...")

        return True  # Seguir en el menú

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = self.pedir_opcion()
            if opcion == -1:
                continue
            continuar = self.ejecutar_opcion()
            if not continuar:
                break


if __name__ == "__main__":
    menu = Menu()
    menu.iniciar()