import xml.etree.ElementTree as ET
from xml.dom import minidom

def generar_xml_salida(campos, ruta_salida, nombre_archivo):
    root = ET.Element("camposAgricolas")

    for campo in campos:
        elem_campo = ET.SubElement(root, "campo", id=campo.id_campo, nombre=campo.nombre)

        # estaciones reducidas
        est_reducidas = ET.SubElement(elem_campo, "estacionesBaseReducidas")
        for est in campo.estaciones:
            ET.SubElement(est_reducidas, "estacion", id=est.id_estacion, nombre=est.nombre)

        # los ensores de suelo
        sen_suelo = ET.SubElement(elem_campo, "sensoresSuelo")
        for ss in campo.sensores_suelo:
            s_elem = ET.SubElement(sen_suelo, "sensorS", id=ss.id_sensor, nombre=ss.nombre)
            for freq in ss.frecuencias:
                f_elem = ET.SubElement(s_elem, "frecuencia", idEstacion=freq.id_estacion)
                f_elem.text = str(freq.valor)

        # los sensores de cultivo
        sen_plantas = ET.SubElement(elem_campo, "sensoresCultivo")
        for st in campo.sensores_plantas:
            t_elem = ET.SubElement(sen_plantas, "sensorT", id=st.id_sensor, nombre=st.nombre)
            for freq in st.frecuencias:
                f_elem = ET.SubElement(t_elem, "frecuencia", idEstacion=freq.id_estacion)
                f_elem.text = str(freq.valor)

    # formato bonito :)
    rough = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough)
    pretty = reparsed.toprettyxml(indent="  ")

    with open(f"{ruta_salida}/{nombre_archivo}", "w", encoding="utf-8") as f:
        f.write(pretty)

    print(f"Archivo de salida generado: {ruta_salida}/{nombre_archivo}")