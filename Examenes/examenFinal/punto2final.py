# Cree una clase humano con atributos nombre, sexo, edad y con la acción
# hablar donde dado un mensaje se mostrará en pantalla. Luego cree una clase Doctor que
# herede de humano y tenga la acción adicional de que dado una estatura y un peso calcule el
# IMC y lo muestre en pantalla.

class Humano ():
    def __init__(self,nombreEntrada,sexoEntrada,edadEntrada):
        print ('Soy un humano nuevo')
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.edad = edadEntrada

    def hablar (self,mensaje):
        print (f'Hola, soy {self.nombre} y quiero ser doctor')

class Doctor (Humano):
    def calcularIMC (self,estaturaEntrada,pesoEntrada):
        pesoIMC = int (input('¿Cuál es tu peso actual en kilogramos?'))
        estaturaIMC = float(input('¿Cuál es tu esatura en metros?'))
        print ('su imc es de: ',pesoIMC/(estaturaIMC**2))

