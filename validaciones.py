bodega={
    "codigo"=int(codigo),
    "nombre"=nombre.strip().lower(),
    "tipo"=tipo.strip().lower(),
    "color_principal"=color.strip().lower(),
    "tamaño"=tamaño.strip().lower(),
    "incluye_tarjeta"=tarjeta.strip().lower(),
    "temporada"=temporada.strip().lower(),
    "precio"=int(precio),
    "unidades"=int(unidades)
}

def mostrar_opcion():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    try:
        opcion=int(input("Seleccione un opción (1-6):\n"))
        return opcion
    except ValueError:
        print("Debe seleccionar una opción válida")
        return -1
    
def unidades_tipo(tipo):
    try:
        unidades=int(input("Cuántas arreglos desea llevar?\n"))
        return unidades>0
    except ValueError:
        return False
    
def busqueda_precio(p_min,p_max):
    p_min=int(input("Ingrese el precio mínimo a buscar:\n"))
    p_max=int(input("Ingrese el precio máximo a buscar:\n"))
    for i in range(p_min,p_max):
        if bodega[i]["precio"]==int(precio):
            return i
    return -1

def buscar_codigo(codigo):
    for i in range(len(bodega)):
        if bodega[i]["codigo"]==int(codigo):
            return i
    return -1

def validar_codigo(codigo):
    try:
        valor=int(codigo)
        return valor>0
    except ValueError:
        return False
    
def validar_unidades(unidades):
    try:
        valor=int(unidades)
        return valor>=0
    except ValueError:
        return False


def agregar_arreglo(codigo,nombre,tipo,color_principal,tamaño,incluye_tarjeta,temporada,precio,unidades)
    cod=int(input("Ingrese el código del arreglo:\n"))
    nom=input("Ingrese el nombre del arreglo:\n")
    tip=input("Ingrese el tipo de arreglo:\n")
    col=input("Ingrese el color principal del arreglo:\n")
    tam=input("Ingrese el tamaño del arreglo:\n")
    tar=input("Ingrese si incluye tarjeta o no (S/N):\n").lower()
    tem=input("Ingrese la temporada del arreglo:\n")
    pre=int(input("Ingrese el precio del arreglo:\n"))
    uni=int(input("Ingrese la cantidad de unidades del arreglo:\n"))
    if not validar_codigo(cod):
        print("[ERROR] el precio tiene que ser un número entero mayor a 0")
        return
    if not validar_unidades(uni):
        print("[ERROR] El número de unidades tiene que ser igual o mayor que 0")
        return
    nuevo_arreglo={
        "codigo":int(cod),
        "nombre":nom.strip(),
        "tipo":tip.strip(),
        "color_principal":col.strip(),
        "tamaño":tam.strip(),
        "incluye_tarjeta":tar.strip().lower(),
        "temporada":tem.strip(),
        "precio":int(pre),
        "unidades":int(uni)
    }
    bodega.append(nuevo_arreglo)
    print("[INFO] Arreglo registrado exitosamente")

def eliminar_arreglo(bodega,codigo):
    for i in range(len(bodega)):
        if bodega[i]["codigo"]==codigo:
            return i
    return -1