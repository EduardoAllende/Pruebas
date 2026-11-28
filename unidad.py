class Unidad:
    def __init__(self,id_unidad,serial,modelo,causa_raiz,debug):
        self.id_unidad = id_unidad
        self.serial = serial
        self.modelo = modelo
        self.causa_raiz = causa_raiz
        self.debug = debug

    def ingresar_unidad(self,id_unidad,serial,modelo,causa_raiz,debug):
        self.id_unidad = id_unidad
        self.serial = serial
        self.modelo = modelo
        self.causa_raiz = causa_raiz
        self.debug = debug

    def mostrar_detalles_de_unidad(self):
        print("********************************************")
        print(f"Id: {self.id_unidad}")
        print(f"Numero de serie: {self.serial}")
        print(f"Modelo: {self.modelo}")
        print(f"Causa Raiz: {self.causa_raiz}")
        print(f"Debug: {self.debug}")
        print("*********************************************")

    def buscar_unidad(self,busqueda):
        return(
            str(self.id_unidad) == busqueda
            or
            str(self.serial) == busqueda
        )
""""
    def modificar_detalles_de_unidad(self):
        self.mostrar_detalles_de_unidad()
        while True:
            print("Que atributo modificara?")
            a = int(input("1-Serial\n2-Modelo\n3-Causa Raiz\n4-Debug\n"))
            if a == 1:
                self.serial = input("Ingrese el numero de serie: ")
            elif a == 2:
                self.modelo = input("Ingrese el modelo: ")
            elif a == 3:
                self.causa_raiz = input("Ingrese la causa raiz: ")
            elif a == 4:
                self.debug = input("Ingrese el debug: ")
            else:
                print("Opcion no valida")
            self.mostrar_detalles_de_unidad()

            if input("Modificar otro atributo?(y/n)").lower() == "y":
                print("OK")
            else:
                break
"""