
from entities.vehiculo import Vehiculo
from entities.multa import Multa
from entities.exceso_velocidad import ExcesoVelocidad
from entities.persona import Persona
from exceptions.excepciones import EntidadYaExiste, InformacionInvalida


class RegistroVehicular:

    def __init__(self):

        self.vehiculos = []
        self.personas= []

    def registrar_vehiculo(self, matricula, nro_padron, cedula_titular):
        
        if matricula == "" or nro_padron == " " or cedula_titular == "":
            raise InformacionInvalida()

        cont = 0
        for persona in self.personas:
            if persona.get_cedula() == cedula_titular:
                if persona.get_libreta_suspendida() == True:
                    raise InformacionInvalida()
                else:
                    cont = 1
                    break

        if cont == 0:
            persona = Persona(cedula_titular, False)
            self.personas.append(persona)
            vehiculo = Vehiculo(matricula, nro_padron)
            self.vehiculos.append(vehiculo)
            # persona.get_vehiculo().append(vehiculo)

        elif cont == 1:
            for vehiculo in self.vehiculos:
                if vehiculo.get_matricula() == matricula:
                    raise EntidadYaExiste()
        
    def get_autos(self):
        for auto in self.vehiculos:
            print(auto.get_matricula())
    
    def get_personas(self):
        for persona in self.personas:
            print(persona.get_cedula())

if __name__ == "__main__":
    
    registro_vehicular = RegistroVehicular()
    registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    try: 
        registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    except Exception as e:
        print(e)
    registro_vehicular.registrar_vehiculo("CBA1234", 3, 12345678)
    registro_vehicular.registrar_vehiculo("CBY1234", 3, 12348278)

    print(registro_vehicular.get_autos())
    print(registro_vehicular.get_personas())