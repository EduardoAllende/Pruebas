# Menu de inicio
mascota = ["","",""]
ciclo = 1
while ciclo:
    opc = int(input("1-Ingresar mascota\n2-Ver mascota\n3-Eliminar mascota\n0-Salir"))
    if opc == 1:
        nombre = input("Introduce el nombre: ")
        mascota[0]=nombre
        raza = input("Introduce el raza: ")
        mascota[1]=raza
        color = input("Introduce el color: ")
        mascota[2]=color
    elif opc == 2:
        print(f"Nombre: {mascota[0]}\nRaza: {mascota[1]}\nColor: {mascota[2]}")
    elif opc == 3:
        mascota[0]=""
        mascota[1]=""
        mascota[2]=""
    else:
        print("bye")
        ciclo = 0


