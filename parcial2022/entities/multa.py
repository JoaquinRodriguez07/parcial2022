
from abc import ABC

class Multa(ABC):
     
    def __init__(self, concepto, importe, esta_paga):
      self.__concepto = concepto
      self.__importe = importe
      self.__esta_paga = esta_paga

    def get_concepto(self):
        return self.__concepto
    
    def get_importe(self):
        return self.__importe
    
    def get_esta_paga(self):
        return self.__esta_paga
    