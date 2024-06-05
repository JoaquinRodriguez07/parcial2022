
from entities.multa import Multa

class ExcesoVelocidad(Multa):

    def __init__(self, velocidad, velocidad_limite, concepto, importe, esta_paga):
        super().__init__(concepto, importe, esta_paga)
        self.__esta_paga = esta_paga
        self.__importe = importe
        self.__concepto = concepto
        self.__velocidad_limite = velocidad_limite
        self.__velocidad = velocidad

    
    def get_velocidad(self):
        return self.__velocidad
    
    def get_velocidad_limite(self):
        return self.__velocidad_limite
    
    def get_concepto(self):
        return self.__concepto
    
    def get_importe(self):
        return self.__importe
    
    def get_esta_paga(self):
        return self.__esta_paga
    
    


