class Persona ():
    def __init__ (self, idEntrada, nombreEntrada, edadEntrada):
        print ('Hola, estoy a tu disposición')
        self.id = idEntrada
        self.nombre = nombreEntrada
        self.edad = edadEntrada
#.....Punto1....#
    def hablar (self, mensaje):
        print (f'soy {self.nombre} y estoy aquí para ti')
    def caminar (self, cantidadPasos):
        for i in range (cantidadPasos):
            print (f'Hoy he caminado {i+1} pasos')
def linedesign(cantidad = 10, simbolo = '#'):
        print (simbolo *cantidad)
        return None
#....Heredar clase Persona para volverla Doctor, Nutricionista y Abogado....#
class Doctor (Persona):
    def __init__(self,idEntrada,nombreEntrada, edadEntrada,especialidadEntrada):
        Persona.__init__(self, idEntrada,nombreEntrada,edadEntrada)
        self.especialidad = especialidadEntrada
    def tratarEnfermedad (self, enfermedad):
        print (f'''Hola, soy {self.nombre}
                especialista en {self.especialidad} y procedo a 
                tratar la {enfermedad} que aqueja al paciente
        ''')

#.......Punto3......#
class Nutricionista (Persona):
    def _init_ (self,idEntrada,nombreEntrada,edadEntrada,universidadEntrada):
        Persona.__init__(self,idEntrada,nombreEntrada,edadEntrada)
        self.universidad = universidadEntrada
    def calcularimc (self,alturaEntrada,pesoEntrada):
        pesoIMC = int (input ('¿Cuál es tu peso actual?'))
        alturaIMC = float (input('¿Cuanto mides en metros?'))
        print ('su imc es de ' ,pesoIMC/(alturaIMC**2))
    def presentarse (self, mensaje1):
        print (f'soy {self.nombre}, tu nutricionista y hoy voy a calcular tu IMC, pero primero debes darme unos datos')
#............Punto4..........#
class Abogado (Persona):
    def __init__(self,idEntrada,nombreEntrada, edadEntrada,especialidadDerecho,universidadAtributo):
        Persona.__init__(self, idEntrada,nombreEntrada,edadEntrada)
        self.especialidadAbogado = especialidadDerecho
        self.sobreMiU = universidadAtributo
    def representarCliente (self,nombreCliente,casoCliente):
        print (f'Soy el abogado {self.nombre} y procedo a representar al cliente {nombreCliente} en su caso de {casoCliente}')

#------Ejecutar-----#
persona1 = Persona (1001548678,'Drew',35)
persona1.hablar ('mensaje')
persona1.caminar (10)
linedesign (3, '.......')
doctor1 = Doctor (1001548900,'Jhonatan',35,'Cardiólogo')
doctor1.tratarEnfermedad ('Miocardiopatía')
linedesign (3, '.......')
nutricionista1 = Nutricionista (123456,'Juan',28)
nutricionista1.presentarse ('.')
nutricionista1.calcularimc (1,2)
linedesign (3, '.......')
abogado1 = Abogado (1001548389,'Julian',47,'Derecho Penal','Convenios con Bufetes Internacionales')
abogado1.representarCliente ('Mauro','Lavado de activos')


