#Inicio------------------------------------------------------
from unidad import Unidad
print("Bienvenido!")
# Variables de conteo o listas
conteo_ids = 0
unidades =[]

def ingresar():
    id = conteo_ids+1
    serial = input("Ingresa el numero de serie de la unidad: ")
    modelo = input("Ingresa el modelo de la unidad: ")
    causa_raiz = input("Ingresa el causa raiz de la unidad: ")
    debug = input("Ingresa el debug de la unidad: ")

    nueva_unidad = Unidad(id,serial,modelo,causa_raiz,debug)
    unidades.append(nueva_unidad)

    print(unidades)

def buscar_unidad(ref):
    for unidad in unidades:
        if unidad.buscar_unidad(ref):
            print("Unidad Encontrada!")
            unidad.mostrar_detalles_de_unidad()
            break



#leer archivos
while True:
    print("*---------------------------------------------*")
    print("Por favor. Selecciona una opcion")
    opc = int(input("1-Ingresar unidad\n2-Detalles de unidad\n3-Modificar unidad\n4-Lista de unidades\n0-Salir\n*---------------------------------------------*\n"))
    if opc == 1:# INGRESAR UNIDAD ------------------------------------------
        print("Ingresando unidad...")
        while True:
            ingresar()
            supopc = input("Los datos ingresados son correctos?(y/n): ").lower()
            if supopc == "n":
                print("Corregiendo...")
            #Modificarunidad(idreciente) - funcion local
            elif supopc == "y":
                print("Unidad agregada exitosamente!")
                conteo_ids += 1
                break
            else:
                print("Opcion no valida")
    elif opc == 2: # DETALLES DE UNIDAD -----------------------------------------
        busqueda = input("ingresa id o numero de serie de la unidad: ").upper()
        print(f"Buscando: {busqueda}")
        buscar_unidad(busqueda)
    elif opc == 3:# MODIFICAR UNIDAD -------------------------------------------
        U = input("ingresa id o numero de serie unidad a modificar: ").upper()
        print(f"Modificando: {U}")
        #BuscarUnidad(U)
        #ModificarUnidad(U)
    elif opc == 4: # LISTA DE UNIDADES -----------------------------------------
        print("Mostrando unidades...")
    elif opc == 0:
        print("Guardando datos de unidades...")
        #Guardar en archivos
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")





