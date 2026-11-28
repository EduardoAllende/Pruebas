#Inicio------------------------------------------------------

print("Bienvenido!")
#leer archivos
while True:
    print("*---------------------------------------------*")
    print("Por favor. Selecciona una opcion")
    opc = int(input("1-Ingresar unidad\n2-Detalles de unidad\n3-Modificar unidad\n4-Lista de unidades\n0-Salir\n*---------------------------------------------*\n"))
    if opc == 1:# INGRESAR UNIDAD ------------------------------------------
        print("Ingresando unidad...")
        #NuevaUnidad() - Funcion local
        #idcount =+ 1
        #MostrarUnidad(idcount) - funcion local
        while True:
            supopc = input("Los datos ingresados son correctos?(y/n): ").lower()
            if supopc == "n":
                print("Corregiendo...")
            #Modificarunidad(idreciente) - funcion local
            elif supopc == "y":
                print("Unidad agregada exitosamente!")
                break
            else:
                print("Opcion no valida")
    elif opc == 2: # DETALLES DE UNIDAD -----------------------------------------
        busqueda = input("ingresa id o numero de serie de la unidad: ").upper()
        print(f"Buscando: {busqueda}")
        #Buscar_unidad(busqueda)
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





