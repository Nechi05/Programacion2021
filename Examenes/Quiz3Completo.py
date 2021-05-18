# PUNTO 1 

# 1.1

class ElementosDigitales():
    def __init__(self, nombre, creador, FechaDePublicacion):
        self.nombre = nombre
        self.creador = creador
        self.FechaDePublicacion = FechaDePublicacion

    def MostrarAtributos (self):
        print('''mis atributos son:
        Nombre -->''', self.nombre, '''
        Creador -->''', self.creador, '''
        Fecha de publicación -->''', self.FechaDePublicacion)

elementosDigitales1 = ElementosDigitales("programa", "Diego", "22/04/2021")
elementosDigitales1.MostrarAtributos()

# 1.2

class Usuario():
    def __init__ (self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada

    def MostrarAtributos (self):
        print(f''' Hola mi nombre es {self.nombre}, tengo
            {self.edad} años y soy {self.nacionalidad}. Me considero
            una persona del sexo {self.sexo} y amante de la música.
    ''')

    def Tocar (self, cancion):
        print (f'''El día de hoy estoy escuchando 
        {cancion}
    ''')

usuario1 = Usuario('Ándres', 23, 'masculino', 'colombiano')
usuario1.MostrarAtributos()
usuario1.Tocar ("El condor herido")

# 1.3  

class Pagina ():
    def __init__(self, TipoDeContenido, formato, FechaDePublicacion):
        self.TipoDeContenido = TipoDeContenido
        self.formato = formato
        self.FechaDePublicacion = FechaDePublicacion

    def MostrarAtributos (self):
        print('''mis atributos son:
        Tipo de contenido -->''', self.TipoDeContenido, '''
        Formato -->''', self.formato, '''
        Fecha de publicación -->''', self.FechaDePublicacion)

pagina1 = Pagina("educativo", "html", "22/04/2021")
pagina1.MostrarAtributos()

# PUNTO 2

#2.1

class Cancion(ElementosDigitales):
    def __init__(self, nombre, creador, FechaDePublicacion, GeneroMusical, DuracionSeg):
        ElementosDigitales.__init__(self, nombre, creador, FechaDePublicacion)
        self.GeneroM = GeneroMusical
        self.DuracionSeg = DuracionSeg

    def MostrarAtributos (self):
        print('''Soy una nueva canción:
        mi nombre es -->''', self.nombre, '''
        fui publicada -->''', self.FechaDePublicacion)

    def bucleCancion (self, repeticiones):
        for numero in range(repeticiones):
            if (numero == 0):
                print (self.nombre, "sonando", numero+1, "vez")
            else:
                print (self.nombre, "sonando", numero+1, "veces")

cancion1 = Cancion("El condor herido", "Diomedez Díaz y Juancho Rois", 1989, "Vallenato", 310)
cancion1.MostrarAtributos ()
cancion1.bucleCancion (3)

# 2.2

class Artista(Usuario):
    def __init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada, generomusicalEntrada, numerocancionesEntrada, numeroalbumEntrada):
        Usuario.__init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada)
        self.generomusical = generomusicalEntrada
        self.numerocanciones = numerocancionesEntrada
        self.numeroalbum = numeroalbumEntrada

    def MostrarAtributos (self):
        print (f''' Mi nombre es {self.nombre}, 
        soy cantante del genero {self.generomusical}. 
        Hasta la fecha tengo {self.numerocanciones}
        canciones en {self.numeroalbum} albumes
        ''')

    def ubicacion (self, ciudad):
        print (f''' El día de mañana 
        daré un concierto en {ciudad},
        los espero.
    ''')

artista = Artista ("Bad Bunny", 25, "hombre", "puerto rico", "trap", 10, 3)
artista.MostrarAtributos ()
artista.ubicacion ("Medellín")

#2.3

class Favoritos (Pagina):
    def __init__ (self, TipoDeContenido, formato, FechaDePublicacion, favoritosComunidad, FechaActualizacion):
        Pagina.__init__ (self, TipoDeContenido, formato, FechaDePublicacion)
        self.favoritosComunidad = favoritosComunidad
        self.FechaActualizacion = FechaActualizacion
    

    def ModificarTemas (self):
        listaFavoritos = []
        listaFavoritos.append (self.favoritosComunidad)
        listaFavoritos.append (self.FechaActualizacion)
        print (listaFavoritos)
        continuar = int(input("si deseas agregar otra canción presiona 1, en caso contrario presiona 2: "))
        while (continuar == 1):
            temaFavorito = str(input("Ingresa la canción que deseas adicionar a la lista: "))
            fechaA = str(input("Ingresa la fecha en que la lista fue actualizada: "))
            listaFavoritos.append (temaFavorito)
            listaFavoritos.append (fechaA)
            print (listaFavoritos)
            continuar = int(input("si deseas  agregar otra canción presiona 1, en caso contrario presiona 2: "))
        print ("Tu lista quedó así", listaFavoritos)
        print ("-------------------")
        preguntaEliminar = int(input("¿deseas eliminar alguna posición? 1- para sí. 2- para no: "))
        while (preguntaEliminar == 1):
            PreguntaEliminarCancion = 'Ingrese la posicion que desea eliminar '
            posicion = int(input(PreguntaEliminarCancion)) - 1
            if (posicion%2 == 0):
                posicion2 = posicion + 1
            else:
                posicion2 = posicion - 1
            listaFavoritos.pop (posicion)
            listaFavoritos.pop (posicion2)
            print (listaFavoritos)
            preguntaEliminar = int(input("¿deseas eliminar otra posición? 1- para sí. 2- para no: "))



favorito1 = Favoritos("Canción", "mp3", "1989", "El condor herido", "22/04/21")
favorito1.ModificarTemas ()
