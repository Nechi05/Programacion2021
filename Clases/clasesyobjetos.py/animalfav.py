class Gato ():
    ''' Esta es la clase Gato, va a tener los siguientes atributos
        nombreEntrada: Nombre del animal 
        edadEntrada: Edad del animal en meses
        colorEntrada: Color del pelaje del animal 
        razaEntrada: Raza del animal
        Y tiene las siguientes acciones:
        *maullar(mensaje):
            dado un mensaje lo mostrará los maullidos en pantalla
        *comer ():
            muestra la cantidad de cuido en gramos que se comerá el gato 
        *caminar ():
            muestra la cantidad de metros que recorrerá el gato por la casa
        *mostrarAtributos()
            muestra los atributos de la mascota
    '''

    def __init__ (self, nombreEntrada,edadEntrada,colorEntrada,razaEntrada):
        print ('Hola soy un gatito nuevo')
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.color = colorEntrada
        self.raza = razaEntrada

    def maullar (self,mensaje):
        print (f'soy {self.nombre}, un {self.raza} y hago ¡MIAAUUU!')
    def mostrarAtributos (self):
        print (f''' Mi nombre es {self.nombre}
                tengo {self.edad} meses
                soy de color {self.color}
                soy un gato {self.raza}
        ''')
    def caminar (self,distanciaMetros):
        for i in range (distanciaMetros):
            print (f'¡MIAU! soy {self.nombre} hoy he recorrido {i+1} metros en la casa')
    def comer (self,gramosCuido,marcaCuido):
        print (f'hoy {self.nombre} ha comido {gramosCuido} gramos de {marcaCuido}')
def linedesign(cantidad = 10, simbolo = '#'):
        print (simbolo *cantidad)
        return None


gato1 = Gato ('Michu',4,'Blanco con negro','Criollo')
gato2 = Gato ('Julieta',48,'Café','Siamés')

gato1.maullar ('Miau')
gato1.mostrarAtributos ()
gato1.caminar (15) 
linedesign (3, '.......')
gato2.maullar ('Miau')
gato2.mostrarAtributos ()
gato2.comer (120,'Mirringo')