from ClaseManejadorPlanesAhorro import ManejadorPlanesAhorro
from claseMenu import Menu

if __name__ == "__main__":
    unManejadorPlanes = ManejadorPlanesAhorro()
    unManejadorPlanes.testPlanes("planes.csv")

    unMenu = Menu()

    unMenu.ejecutarMenu(unManejadorPlanes)