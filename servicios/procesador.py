from clases.estacion import Estacion
from clases.frecuencia import Frecuencia
from listas.lista_enlazada import ListaEnlazada


def procesar_campos(campos):
    for campo in campos:
        print(f"\n Procesando campo: {campo.nombre}")

        # lista de grupos
        grupos = ListaEnlazada()

        for est_actual in campo.estaciones:
            huella_suelo = _obtener_huella(campo.sensores_suelo, est_actual.id_estacion)
            huella_plantas = _obtener_huella(campo.sensores_plantas, est_actual.id_estacion)
            huella_completa = f"Suelo:{huella_suelo}|Plantas:{huella_plantas}"

            print(f"   Estación {est_actual.id_estacion} -> Huella: {huella_completa}")

            # buscar si ya existe un grupo con esta huella
            grupo_encontrado = None
            for grupo in grupos:
                if grupo[0] == huella_completa:
                    grupo_encontrado = grupo
                    break

            if grupo_encontrado:
                grupo_encontrado[1].agregar(est_actual)
                print(f"   → Agrupada con patrón existente")
            else:
                nuevas_estaciones = ListaEnlazada()
                nuevas_estaciones.agregar(est_actual)
                grupos.agregar((huella_completa, nuevas_estaciones))
                print(f"   → Nuevo grupo creado")

        # creamos nuevas estaciones como reducidads
        nuevas_estaciones = ListaEnlazada()
        mapeo = {}
        contador = 1

        print(f"\n Grupos encontrados:")
        for grupo in grupos:
            huella, lista_estaciones = grupo
            nuevos_nombres = []
            for est in lista_estaciones:
                nuevos_nombres.append(est.nombre)
            print(f"   Grupo {contador}: {', '.join(nuevos_nombres)}")

            nuevo_id = f"e{contador}"
            nombre_combinado = ", ".join(nuevos_nombres)
            nuevas_estaciones.agregar(Estacion(nuevo_id, nombre_combinado))

            for est in lista_estaciones:
                mapeo[est.id_estacion] = nuevo_id

            contador += 1

        # actualizsmos las frecuencias en sensores
        for sensor in campo.sensores_suelo:
            nuevas_freqs = {}
            for freq in sensor.frecuencias:
                nuevo_id = mapeo[freq.id_estacion]
                nuevas_freqs[nuevo_id] = nuevas_freqs.get(nuevo_id, 0) + freq.valor
            # reconstruir lista
            sensor.frecuencias = ListaEnlazada()
            for nid, val in nuevas_freqs.items():
                sensor.frecuencias.agregar(Frecuencia(nid, val))

        for sensor in campo.sensores_plantas:
            nuevas_freqs = {}
            for freq in sensor.frecuencias:
                nuevo_id = mapeo[freq.id_estacion]
                nuevas_freqs[nuevo_id] = nuevas_freqs.get(nuevo_id, 0) + freq.valor
            sensor.frecuencias = ListaEnlazada()
            for nid, val in nuevas_freqs.items():
                sensor.frecuencias.agregar(Frecuencia(nid, val))

        # reemplazar estaciones 
        campo.estaciones = nuevas_estaciones
        print(f"\n Campo {campo.nombre} procesado. Estaciones reducidas a {len(nuevas_estaciones)}.")
    return campos


def _obtener_huella(sensores, id_estacion):
        # devuelve una cadena que representa el patrón binario de conexion
        # 1 = hay frecuencia 0 = no hay frecuencia
    partes = []
    for sensor in sensores:
        hay_frecuencia = False
        for freq in sensor.frecuencias:
            if freq.id_estacion == id_estacion:
                hay_frecuencia = True
                break
        partes.append(f"{sensor.id_sensor}:{1 if hay_frecuencia else 0}")
    return "|".join(partes)