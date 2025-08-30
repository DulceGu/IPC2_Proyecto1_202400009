from graphviz import Source
import os

# lass arpetas para guardar gráficas
RUTA_DOT = "salidas/dot"
RUTA_PNG = "salidas/png"

os.makedirs(RUTA_DOT, exist_ok=True)
os.makedirs(RUTA_PNG, exist_ok=True)


def generar_grafica(campos_originales, campos_procesados):
    if not campos_originales:
        print("No hay campos cargados.")
        return

    # Mostrar campos
    print("\nCampos disponibles:")
    for i, c in enumerate(campos_originales):
        print(f"{i+1}. {c.nombre}")

    try:
        idx = int(input("Seleccione un campo: ")) - 1
        if idx < 0 or idx >= len(campos_originales):
            print("Índice inválido.")
            return
        campo_orig = campos_originales[idx]
        campo_proc = campos_procesados[idx]
    except:
        print("Entrada inválida.")
        return

    print("\nTipos de gráfica:")
    print("1. Matriz Frecuencia Suelo (Original)")
    print("2. Matriz Frecuencia Cultivo (Original)")
    print("3. Matriz Patrones Suelo")
    print("4. Matriz Patrones Cultivo")
    print("5. Matriz Reducida Suelo")
    print("6. Matriz Reducida Cultivo")

    try:
        opcion = int(input("Seleccione (1-6): "))
    except:
        print("Opción inválida.")
        return

    # datos segunt u opcion
    if opcion in [1, 3, 5]:
        sensores = campo_orig.sensores_suelo if opcion == 1 else campo_proc.sensores_suelo
        estaciones = campo_orig.estaciones if opcion == 1 else campo_proc.estaciones
        titulo = "Frecuencia Suelo" if opcion == 1 else "Patrón Suelo" if opcion == 3 else "Reducida Suelo"
        color = "#e8f5e8" if opcion == 1 else "#f3e8f5" if opcion == 3 else "#fff3e0"
    else:
        sensores = campo_orig.sensores_plantas if opcion == 2 else campo_proc.sensores_plantas
        estaciones = campo_orig.estaciones if opcion == 2 else campo_proc.estaciones
        titulo = "Frecuencia Cultivo" if opcion == 2 else "Patrón Cultivo" if opcion == 4 else "Reducida Cultivo"
        color = "#e8f5f5" if opcion == 2 else "#f0f5e8" if opcion == 4 else "#f5e8e8"

    # función para obtener valor
    def obtener_valor(sensor, id_estacion):
        for freq in sensor.frecuencias:
            if freq.id_estacion == id_estacion:
                return str(freq.valor)
        return "0"

    def hay_patron(sensor, id_estacion):
        for freq in sensor.frecuencias:
            if freq.id_estacion == id_estacion:
                return "1"
        return "0"

    valor_fn = hay_patron if opcion in [3, 4] else obtener_valor

    # creamos la tabla html
    label = f'''<table border="1" cellborder="1" cellspacing="0" cellpadding="6">
<tr><td bgcolor="#f0f0f0"><b>Estación\\Sensor</b></td>'''
    for s in sensores:
        label += f'<td bgcolor="#e8e8e8"><b>{s.id_sensor}</b></td>'
    label += '</tr>'

    for est in estaciones:
        label += f'<tr><td bgcolor="#e8e8e8"><b>{est.id_estacion}</b></td>'
        for sensor in sensores:
            valor = valor_fn(sensor, est.id_estacion)
            bg = "#f0d0e4" if int(valor) > 0 else "#ffffff"
            label += f'<td bgcolor="{bg}">{valor}</td>'
        label += '</tr>'
    label += '</table>'

    # codigo DOT
    dot_code = f'''digraph G {{
    rankdir = "TB";
    node [shape = none, fontname = "Arial"];
    
    titulo [label = "Campo: {campo_orig.nombre}\\n{titulo}", fontsize = "18"];
    
    matriz [label = <{label}>, shape = plain];
    
    titulo -> matriz [style = invis];
}}'''

    # nombre de archivo
    nombre = f"matriz_{opcion}_campo_{campo_orig.id_campo}"
    ruta_dot = os.path.join(RUTA_DOT, f"{nombre}.dot")
    ruta_png = os.path.join(RUTA_PNG, nombre)

    # guardamos en un .dot
    with open(ruta_dot, 'w', encoding='utf-8') as f:
        f.write(dot_code)

    # generamos la imagen png
    try:
        src = Source(dot_code)
        src.render(ruta_png, format='png', cleanup=True, view=True)
        print(f"\n Gráfica generada: {ruta_png}.png")
    except Exception as e:
        print(f"\n Error al generar gráfica: {e}")