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
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en mts? : "
MENSAJE_RESULTADO = "El resultado de la prueba de obesidad es..."
MENSAJE_BAJO_PESO = "Estas bajo de peso"
MENSAJE_ADECUADO = "Estás dentro de tu peso ideal"
MENSAJE_SOBREPESO = "Ten cuidado, estas en sobrepeso"
MENSAJE_OBESO = "Cuidado! estás obeso, tu salud corre riesgo"
class Nutricionista (Persona):
    def _init_ (self,idEntrada,nombreEntrada,edadEntrada,universidadEntrada):
        Persona.__init__(self,idEntrada,nombreEntrada,edadEntrada)
        self.universidad = universidadEntrada
    def calcularimc (self,resultado):
        peso = float(input(PREGUNTA_PESO))
        estatura = float(input(PREGUNTA_ESTATURA))
        imc = peso/(estatura**2)
        isBajoPeso = imc < 18.5
        isAdecuado = imc >= 18.5 and imc < 25
        isSobrepeso = imc >= 25 and imc < 30
        resultado = ""
        if(isBajoPeso):
            resultado=(MENSAJE_BAJO_PESO)
        elif(isAdecuado):
            resultado=(MENSAJE_ADECUADO)
        elif(isSobrepeso):
            resultado=(MENSAJE_SOBREPESO)
        else:
            resultado=(MENSAJE_OBESO)
        print (f'''Hola, soy tu nutricionista {self.nombre}
                egresada de la universidad {self.universidad}
                tu imc es de {resultado}
                ''')
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
#error nutri
linedesign (3, '.......')
abogado1 = Abogado (1001548389,'Julian',47,'Derecho Penal','Convenios con Bufetes Internacionales')
abogado1.representarCliente ('Mauro','Lavado de activos')
