from ClasePlanAhorro import PlanAhorro
import csv

class ManejadorPlanesAhorro:
    __lista = []

    def __init__(self):
        self.__lista = []
    

    def agregarPlan(self, unPlan):
        if isinstance(unPlan, PlanAhorro):
            self.__lista.append(unPlan)
        else:
            print("[ERROR] No se puede agregar un objeto del tipo {0}".format(type(unPlan)))
    
    
    def testPlanes(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[3].isdecimal() and fila[4].isdecimal() and fila[5].isdecimal():
                unPlan = PlanAhorro(int(fila[0]), fila[1], fila[2], int(fila[3]))
                self.agregarPlan(unPlan)
                PlanAhorro.setCuotasTotales(int(fila[4]))
                PlanAhorro.setCuotasLicitar(int(fila[5]))
        archivo.close()

    
    def setValores(self):
        for unPlan in self.__lista:
            print(unPlan)
            valor = int(input("Ingrese el nuevo valor del vehiculo: "))
            unPlan.setValorVehiculo(valor)
    

    def buscarPlanPorCodigo(self, codigo):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getCodigoPlan() != codigo:
            i += 1
        if i == len(self.__lista):
            i = -1
        return i


    def getMontoLicitarVehiculo(self, codigo):
        indice = self.buscarPlanPorCodigo(codigo)
        if indice != -1:
            unPlan = self.__lista[indice]
        else:
            unPlan = None
            print("[ERROR] No hay un vehiculo con el codigo {0}".format(codigo))
        return PlanAhorro.getCuotasLicitar() * unPlan.getValorCuota()


    def mostrarVehiculosPorValorCuotaMenor(self, valor):
        print("Vehiculos con valor menor al dado:")
        for unPlan in self.__lista:
            if unPlan.getValorCuota() < valor:
                print(unPlan)
    
    
    def guardarCambios(self, nombreArchivo):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo, delimiter=";")
        for unPlan in self.__lista:
            if isinstance(unPlan, PlanAhorro):
                writer.writerow([unPlan.getCodigoPlan(), unPlan.getModelo(), unPlan.getVersion(), unPlan.getValorVehiculo(), PlanAhorro.getCuotasTotales(), PlanAhorro.getCuotasLicitar()])
        archivo.close()