class Humano ():
    '''
    Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        estaturaEntrada: Hace referencia al estatura del usuario
        Tiene las siguientes acciones:
        *hablar(mensaje):
            dado un mensaje lo muestra en pantalla
        
        *mostrarAtributos()
            muestra los atributos del usuario
    '''

    def __init__ (self,nombreEntrada,edadEntrada,estaturaEntrada):
        print ('Hola soy un humano nuevo..')
        self.edad = edadEntrada
        self.especie = 'Humana'
        self.nombre = nombreEntrada
        self.estatura = estaturaEntrada
        self.dinero = 0


    def hablar (self,mensaje):
        print (f'Hola soy {self.nombre} tengo un mensaje que decir...')
    def mostrarAtributos (self):
        print (f''' Mi nombre es {self.nombre}
                mi estatura {self.estatura}
                mi edad {self.edad}
        ''')
    def mostrarAtributos(self):
            print(f'''Mi nombre es {self.nombre}
                        Mi estatura es {self.estatura} metros
                        Mi edad es {self.edad} años
                        Tengo ahorrado {self.dinero} pesos
            ''')
    def recorrerDistancia (self,distanciaMetros):
        for i in range (distanciaMetros):
            print (f'Hola soy {self.nombre} y he recorrido {i+1} metros')

    def ahorraDinero (self,):
        preguntaIngresarMontos = 'Ingrese S--> para continuar añadiento montos y N---> para finalizar '
        preguntaMonto = 'Cuanto vas a ingresar?: '
        ingresarMontos = input (preguntaIngresarMontos)
        while (ingresarMontos != 'N'):
            monto = float (input (preguntaMonto))
            self.dinero = self.dinero + monto
            print (f'Soy {self.nombre} y tengo {self.dinero} pesos')
            ingresarMontos = input (preguntaIngresarMontos)
        return self.dinero 

class Biomedico ( Humano ):
    def mantenimientoEquiposMedicos (self, nombreEquipo):
        print (f'Hola soy {self.nombre} y procedo a arreglar el {nombreEquipo}')


humano1 = Humano('Abraham',21,1.84)
humano2 = Humano('David',19,1.76)

humano1.hablar ('Espero esten muy bien ')
humano2.hablar ('chau')
print (humano1.nombre)
print (humano2.nombre)
print (humano2.edad)
humano1.mostrarAtributos ()
humano1.recorrerDistancia (30)
humano2.mostrarAtributos
totalAhorrado = humano2.ahorraDinero()
humano2.mostrarAtributos ()
biomedico = Biomedico ('Duvan',20,1.85)
biomedico.mostrarAtributos ()
biomedico.mantenimientoEquiposMedicos ('Electrocardiograma')