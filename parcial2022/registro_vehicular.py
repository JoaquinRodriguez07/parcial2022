
from entities.vehiculo import Vehiculo
from entities.multa import Multa
from entities.exceso_velocidad import ExcesoVelocidad
from entities.persona import Persona
from exceptions.excepciones import EntidadYaExiste, InformacionInvalida, EntidadNoExiste


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
            vehiculo.set_persona(persona)


        elif cont == 1:
            for vehiculo in self.vehiculos:
                if vehiculo.get_matricula() == matricula:
                    raise EntidadYaExiste()
        
    def get_autos(self):
        for auto in self.vehiculos:
            p = auto.get_persona()
            print(p.get_cedula())
    
    def get_personas(self):
        for persona in self.personas:
            print(persona.get_cedula())
    

    def registrar_multa_vehiculo(self,matricula, concepto, importe, es_exceso_velocidad, velocidad_vehiculo, velocidad_limite):

        if matricula == "" or concepto == "" or importe == "" or  es_exceso_velocidad == "" or velocidad_vehiculo == "" or velocidad_limite == "":
            raise InformacionInvalida()
        
        cont = 0
        for auto in self.vehiculos:
            if auto.get_matricula() == matricula:
                cont = 1    
                if es_exceso_velocidad == True:
                    multa_exceso = ExcesoVelocidad(velocidad_vehiculo, velocidad_limite, concepto, importe, False)
                    multas_auto = auto.get_multa()
                    multas_auto.append(multa_exceso)
                    car = auto
                    break
                else:
                    multas_auto = auto.get_multa()
                    multas_auto.append(Multa(concepto, importe, False))
                    car = auto
                    break
        
        if cont == 0:
            raise EntidadNoExiste()
        
        cont2 = 0
        cont2 = 0
        for multa in car.get_multa():
            if isinstance(multa, ExcesoVelocidad):
                cont2 += 1
        
        if cont2 >= 3:
            person = car.get_persona()
            person.set_libreta_suspendida()

    def get_multas(self):
        for auto in self.vehiculos:
            if auto.get_matricula() == "ABC1234":
                multas = auto.get_multa()
                break
        cont = 0
        for multa in multas:
            if multa is not None:
                cont += 1
                print(multa.get_esta_paga())

        if cont == 0:
            print("El vehiculo no tiene multas")
    
    def pagar_multa_vehiculo(self, matricula, concepto, importe):

        cont = 0 
        for auto in self.vehiculos:
            if auto.get_matricula() == matricula:
                cont += 1
                nave = auto
                break
        
        if cont == 0:
            raise EntidadNoExiste()

        elif cont >=1:
            for multa in nave.get_multa():
                if multa.get_concepto() == concepto and multa.get_importe() == importe and multa.get_esta_paga()==False:
                    multa.set_esta_paga()
                    break
    
    def traspaso_vehiculo(self, cedula_titular, matricula, cedula_nuevo_titular):

        cont = 0
        for persona in self.personas:
            if persona.get_cedula() == cedula_nuevo_titular:
                new_prop = persona
                cont +=1
                break
        
        if cont == 0:
            raise EntidadNoExiste()
        cont2 = 0
        for per in self.personas:
            if per.get_cedula() == cedula_titular:
                old_prop = per
                cont2 +=1
                break
        
        if cont2 == 0:
            raise EntidadNoExiste
        
        for auto in self.vehiculos:
            if auto.get_persona() == old_prop:
                auto.set_persona(new_prop)
                break
        



if __name__ == "__main__":
    
    registro_vehicular = RegistroVehicular()
    registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    try: 
        registro_vehicular.registrar_vehiculo("ABC1234", 2, 12345678)
    except Exception as e:
        print(e)
    registro_vehicular.registrar_vehiculo("CBA1234", 3, 12345678)
    registro_vehicular.registrar_vehiculo("CBY1234", 3, 12348278)

    registro_vehicular.get_autos()
    
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234, True, 65, 60)
    registro_vehicular.registrar_multa_vehiculo("ABC1234", "Mal estacionamiento", 12334, False, None, None)
    registro_vehicular.pagar_multa_vehiculo("ABC1234", "Exceso de velocidad", 1234)
    registro_vehicular.get_multas()
    
    registro_vehicular.traspaso_vehiculo(12345678, "CBY1234", 12348278)
    
    registro_vehicular.get_autos()


