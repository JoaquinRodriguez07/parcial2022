

class Vehiculo:

    def __init__(self, matricula, padron):
        self.__matricula = matricula
        self.__padron = padron
        self.persona = []
    

    def get_matricula(self):
        return self.__matricula
    
    def get_padron(self):
        return self.__padron
    
    def get_persona(self):
        return self.persona
    