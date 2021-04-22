class Pagina ():
    def __init__ (self, tipoContenido,formatoEntrada,fechaPublicacion):
        self.contenido = tipoContenido
        self.formato = formatoEntrada
        self.fecha = fechaPublicacion
    def mostrarAtributos (self):
        print (f'''Esta es un página de {self.contenido}, en {self.formato} 
        y salió a la web en esta fecha: {self.fecha}''')

#...........Punto2............#
class Favoritos (Pagina):
    def _init_ (self,tipoContenido,formatoEntrada,fechaPublicacion,favoritosComunidad,ultimaActualizacion):
        Pagina.__init__(self,tipoContenido,formatoEntrada,fechaPublicacion)
        self.favoritos = favoritosComunidad
        self.actualizacion = ultimaActualizacion

def temasFavoritos (new):
        a=0
        b=1
        listafavoritos = []
        while a < new:
            print (a, end = '')
            a = b
            b = a+b
            listafavoritos.append (b)
        print (listafavoritos)
        ingresar = int(input ('Ingresa tu nueva canción favorita: ')) 
        suma = 0
        for i in listafavoritos:
            if ingresar == listafavoritos:
                print ('el numero {} se encuentra en la posicion {}'.format(ingresar,i))
            else:
                print ('el numero {} no se encuentra en la posicion {}'.format(ingresar,i))
temasFavoritos (1000)

#...........Eliminar.........#
listafavoritos = []
PreguntaEliminarCancion = 'Ingrese la posicion que desea eliminar '
print (listafavoritos)
posicion = int(input(PreguntaEliminarCancion)) - 1
listafavoritos.pop (posicion)
print (listafavoritos)

