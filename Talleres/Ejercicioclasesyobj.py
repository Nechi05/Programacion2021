class Torta ():
    '''
    Esta clase tiene los siguientes atributos:
        Forma: habla de la forma de la torta con una figura geométrica
        Sabor: el sabor de la torta
        Altura: altura de la torta en centímetros
        *mostrarAtributos()
            muestra los atributos del usuario
    '''
    def __init__ (self,formaEntrada,saborEntrada,alturaEntrada):
        print ('Domicilio de la pastelería TortiTorti')
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada

    def mostrarAtributos (self):
        print (f'''
        Esta es una torta en forma de {self.forma}
        con a sabor {self.sabor} y tiene {self.altura} cm de altura
        ''')

#-----------Punto2----------#
class Estudiante ():
    def __init__ (self,edadEntrada,nombreEntrada,idEntrada,carreraEntrada,semestreEntrada):
        print ('soy un estudiante nuevo')
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestreEntrada = semestreEntrada
    def mostrarAspiracion (self,asignatura,tiempoEstudio):
        '''
        asignatura: Cualquier asignatura del plan de estudios de la respectiva carrera.
        tiempoEstudio: tiempo que le tomará cursar la materia en SEMANAS.
        '''
        print (f'''
        Hola soy {self.nombre}, tengo {self.edad} y soy estudiante de {self.carrera}
        este semestre voy a ver {asignatura} y me tomará {tiempoEstudio} semanas cursarla
        ''')

#--------Punto3--------#
class Nutriologo ():
    def __init__ (self, edadEntrada,nombreEntrada,universidadEntrada):
        self.edad =edadEntrada
        self.nombre =nombreEntrada
        self.universidad = universidadEntrada
        print (f'soy {self.nombre}, tu nutricionista, egresado de la universidad {self.universidad} y hoy voy a calcular tu IMC, pero primero debes darme unos datos')
    def calcularimc (self,nombrePaciente):
        pesoIMC = int (input (f'{nombrePaciente}, ¿Cuál es tu peso actual?'))
        alturaIMC = float (input(f'{nombrePaciente}¿Cuanto mides en metros?'))
        print ('su imc es de ' ,(pesoIMC/alturaIMC**2))

#Ejecutar#
nutriologo1 = Nutriologo (24,'Andrés','CES')
nutriologo1.calcularimc ('Julián')
torta1 = Torta ('cuadrada','fresa',30)
torta1.mostrarAtributos ()