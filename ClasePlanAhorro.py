class PlanAhorro:
    __cuotasTotales = 1
    __cuotasLicitar = 1
    __codigoPlan = ""
    __modelo = ""
    __version = ""
    __valorVehiculo = 0

    def __init__(self, codigoPlan, modelo, version, valorVehiculo):
        self.__codigoPlan = codigoPlan
        self.__modelo = modelo
        self.__version = version
        self.__valorVehiculo = valorVehiculo

    
    @classmethod
    def getCuotasTotales(cls):
        return cls.__cuotasTotales
    
    @classmethod
    def getCuotasLicitar(cls):
        return cls.__cuotasLicitar
    
    @classmethod
    def setCuotasTotales(cls, cuotas):
        seteado = False
        if isinstance(cuotas, int):
            cls.__cuotasTotales = cuotas
            seteado = True
        return seteado
    
    @classmethod
    def setCuotasLicitar(cls, cuotas):
        seteado = False
        if isinstance(cuotas, int):
            cls.__cuotasLicitar = cuotas
            seteado = True
        return seteado
    
    def getCodigoPlan(self):
        return self.__codigoPlan
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValorVehiculo(self):
        return self.__valorVehiculo
    
    def setValorVehiculo(self, valor):
        seteado = False
        if isinstance(valor, float) or isinstance(valor, int):
            self.__valorVehiculo = valor
            seteado = True
        return seteado


    def getValorCuota(self):
        return self.getValorVehiculo()/self.getCuotasTotales() + self.getValorVehiculo() * 0.1
    
    def __str__(self):
        return "Codigo del plan: {0}\nModelo del vehiculo: {1}\nVersion del vehiculo: {2}\n".format(self.getCodigoPlan(), self.getModelo(), self.getVersion())
