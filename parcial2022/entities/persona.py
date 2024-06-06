
class Persona:

    def __init__(self, cedula, libreta_suspendida):
        self.__cedula =  cedula
        self.__libreta_suspendida = libreta_suspendida
        self.vehiculos = []
    
    #getters
    def get_cedula(self):
        return self.__cedula
    
    def get_libreta_suspendida(self):
        return self.__libreta_suspendida
    
    def get_vehiculo(self):
        return self.vehiculos
    
    #Setters
    def set_libreta_suspendida(self):
        self.__libreta_suspendida = True
    