import validaciones as vld
def main():
    arreglos=[
        "codigo"={},
        "nombre"={},
        "tipo"={},
        "color_principal"={},
        "tamaño"={},
        "incluye_tarjeta"={},
        "temporada"={},
        "precio"={}
        "unidades"={}
    ]
    while True:
        vld.mostrar_opcion()
        opcion=vld.leer_opcion()
        if opcion==1:
            print("===== Unidades por tipo de arreglo =====")
            tipo=input("Qué tipo de arreglo desea?\n").strip().lower()
            unidades=vld.unidades_tipo()
        elif opcion==2:
            print("===== Busqueda de arreglos por precio =====")
            vld.busqueda_precio()

        elif opcion==3:
            print("===== Actualizar arreglo =====")

        elif opcion==4:
            print("===== Agregar arreglos =====")
            vld.agregar_arreglo(arreglos)

        elif opcion==5:
            print("===== Eliminar arreglos =====")
            vld.eliminar_arreglo(arreglos)
            eliminar=int(input("Ingrese el código del arreglo a eliminar:\n"))
            posicion=vld.buscar_codigo(arreglos,eliminar)
            if posicion!=-1:
                arreglos.pop(posicion)
                print(f"El arreglo {eliminar} ha sido eliminado del sistema")
            else:
                print(f"El arreglo {eliminar} no se encuentra registrado")

        elif opcion==6:
            print("Programa finalizado.")
            break

if __name__=="__main__":
    main()

