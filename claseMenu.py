from ClaseManejadorPlanesAhorro import ManejadorPlanesAhorro
from ClasePlanAhorro import PlanAhorro

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                          }

    def mostrarOpciones(self):
        print("[1] Actualizar los valores de los vehiculos")
        print("[2] Mostrar vehiculos con valor menor a uno dado por teclado")
        print("[3] Mostrar monto a pagar para licitar un vehiculo dado su codigo de plan")
        print("[4] Modificar la cantidad de cuotas a pagar para licitar")
        print("[5] Salir")

    def opcion(self, unManejadorPlanes, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3' or op == '5':
            func(unManejadorPlanes)
        else:
            func()


    def salir(self, unManejadorPlanes):
        if isinstance(unManejadorPlanes, ManejadorPlanesAhorro):
            unManejadorPlanes.guardarCambios("planes actualizados.csv")
        print('Usted salio del programa')


    def opcion1(self, unManejadorPlanes):
        if isinstance(unManejadorPlanes, ManejadorPlanesAhorro):
            unManejadorPlanes.setValores()


    def opcion2(self, unManejadorPlanes):
        if isinstance(unManejadorPlanes, ManejadorPlanesAhorro):
            valor = int(input("Ingrese el valor para mostrar los vehiculos con valor de cuota inferior: "))
            unManejadorPlanes.mostrarVehiculosPorValorCuotaMenor(valor)


    def opcion3(self, unManejadorPlanes):
        if isinstance(unManejadorPlanes, ManejadorPlanesAhorro):
            codigo = int(input("Ingrese el codigo del plan para consultar el monto para licitar el vehiculo: "))
            monto = unManejadorPlanes.getMontoLicitarVehiculo(codigo)
            print("El monto para licitar el vehiculo es de ${0:.2f}".format(monto))
    

    def opcion4(self):
        cuotas = int(input("Ingrese la cantidad de cuotas que debe tener pagas para licitar: "))
        PlanAhorro.setCuotasLicitar(cuotas)

    def ejecutarMenu(self, unManejadorPlanes):
        opcion = "0"
        while opcion != '5':
            self.mostrarOpciones()
            opcion = input("--> ")
            self.opcion(unManejadorPlanes, opcion)
        