import xml.etree.ElementTree as ET
from clases.campo_agricola import CampoAgricola
from clases.estacion import Estacion
from clases.sensor_suelo import SensorSuelo
from clases.sensor_plantas import SensorPlantas
from clases.frecuencia import Frecuencia
from listas.lista_enlazada import ListaEnlazada

def cargar_campos_desde_xml(ruta_archivo):
    try:
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        campos = []

        for elem_campo in root.findall("campo"):
            id_campo = elem_campo.get("id")
            nombre_campo = elem_campo.get("nombre")
            campo = CampoAgricola(id_campo, nombre_campo)

            # cargar estaciones
            for elem_est in elem_campo.find("estacionesBase").findall("estacion"):
                estacion = Estacion(elem_est.get("id"), elem_est.get("nombre"))
                campo.estaciones.agregar(estacion)

            # cargar sensores de suelo
            for elem_ss in elem_campo.find("sensoresSuelo").findall("sensorS"):
                sensor = SensorSuelo(elem_ss.get("id"), elem_ss.get("nombre"))
                for freq in elem_ss.findall("frecuencia"):
                    id_est = freq.get("idEstacion")
                    valor = freq.text.strip()
                    frecuencia = Frecuencia(id_est, valor)
                    sensor.frecuencias.agregar(frecuencia)
                campo.sensores_suelo.agregar(sensor)

            # cargar sensores de cultivo (plantas)
            for elem_st in elem_campo.find("sensoresCultivo").findall("sensorT"):
                sensor = SensorPlantas(elem_st.get("id"), elem_st.get("nombre"))
                for freq in elem_st.findall("frecuencia"):
                    id_est = freq.get("idEstacion")
                    valor = freq.text.strip()
                    frecuencia = Frecuencia(id_est, valor)
                    sensor.frecuencias.agregar(frecuencia)
                campo.sensores_plantas.agregar(sensor)

            campos.append(campo)
            print(f"*** Cargando campo agricola {nombre_campo}")

        return campos

    except Exception as e:
        print(f" :c Error al cargar el archivo: {e}")
        return []