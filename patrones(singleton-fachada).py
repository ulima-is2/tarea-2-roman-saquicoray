import sys
import sqlite3

conn = sqlite3.connect ('patrones.db')
c.execute('''CREATE TABLE entradas(codigo_entrada text, cine text, pelicula_elegida text, funcion_elegida text, cantidad_entradas integer)''')

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    instance = None
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Singleton()
        return cls.instance

class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula.get_instance()
        peliculaHF = Pelicula.get_instance()
        peliculaD = Pelicula.get_instance()
        peliculaDeep = Pelicula.get_instance()

        peliculaIT._id = 1
        peliculaIT._nombre = 'IT'
        peliculaIT._id = 2
        peliculaIT._nombre = 'La Hora Final'
        peliculaIT._id = 3
        peliculaIT._nombre = 'Desparecido'
        peliculaIT._id = 4
        peliculaIT._nombre = 'Deep El Pulpo'

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class CineStark:
    def __init__(self):
        peliculaD = Pelicula.get_instance()
        peliculaDeep = Pelicula.get_instance()

        peliculaD._id = 1
        peliculaD._nombre = 'Desparecido'
        peliculaDeep._id = 2
        peliculaDeep._nombre = 'Deep El Pulpo'

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class GestorOpciones:
    def __init__(self):
        self.opciones = Opciones()
        self.opcion1y2 = Opcion1y2()
        self.opcion3 = Opcion3()
        self.opciones.set_sucesor(self.opcion1y2)
        self.opcion1y2.set_sucesor(self.opcion3)
    def desplegar_opciones(self, numero):
        self.opciones.obtener_opciones(numero)

class OpcionTemp:
    def set_sucesor(self,sucesor):
        self.sucesor = sucesor
    def obtener_opciones(self, numero):
        pass

class Opciones(OpcionesTemp):
    def obtener_opciones(self, numero):
        if numero.opciontemp < 1:
            print('Ingrese la opción que desea realizar')
            print('(1) Listar cines')
            print('(2) Listar cartelera')
            print('(3) Comprar entrada')
            print('(0) Salir')
            return True
        else:
            return self.sucesor.obtener_opcion(numero)

class Opcion1y2:
    def obtener_opciones(self, numero):
        if numero.opciontemp < 3:
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            return True
        else:
            return self.sucesor.obtener_opcion(numero)

class Opcion3:
    def obtener_opciones(self, numero):
        if numero.opciontemp < 3:
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            return True

class Numero:
    def __init__(self, opciontemp):
        self.opciontemp = opciontemp

def main():
    terminado = False;
    factory = OpcionesFactory()
    while not terminado:
        numero = Numero(0)
        gestor = GestorOpciones()
        gestor.desplegar_opciones(numero)
        opcion = input('Opción: ')
        if opcion == '1':
            numero = Numero(opcion)
            gestor = GestorOpciones()
            gestor.desplegar_opciones(numero)
        elif opcion == '2':
            numero = Numero(opcion)
            gestor = GestorOpciones()
            gestor.desplegar_opciones(numero)
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()
            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')
        elif opcion == '3':
            numero = Numero(opcion)
            gestor = GestorOpciones()
            gestor.desplegar_opciones(numero)
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()
            peliculas = cine.listar_peliculas()
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
            c.execute('''INSERT INTO entradas(codigo_entrada, cine, pelicula_elegida, funcion_elegida, cantidad_entradas)''')
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)

if __name__ == '__main__':
    main()
