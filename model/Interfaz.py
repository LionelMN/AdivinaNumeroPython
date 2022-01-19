from model.JuegoNumeroSecreto import JuegoNumeroSecreto

'''
 Interfaz del juego Adivinar el número
'''
class Interfaz:
    juego: JuegoNumeroSecreto

    '''
     Constructor de la clase
     Inicializa juego
    '''
    def __init__(self) -> None:
        self.juego = JuegoNumeroSecreto()
        pass

    '''
     Método que inicia el juego
     Pregunta al jugador en bucle para que introduzca por una de las opciones válidas del juego
     Se acaba cuando el jugador sale, consume todos los intentos o gana el juego
     En caso de que se termine el juego por otra razón que no sea que salió de este, se le pregunta si quiere volver a jugar
    '''
    def iniciar(self) -> None:
        opcion : int = 1
        while(opcion != 6 and self.juego.haTerminado() == False and self.juego.getIntentos() < self.juego.getMaxIntentos()):
            opcion = self.leerNumero()
            if(opcion >= 1 and opcion <=6):
                if(opcion == 1):
                    print("Introduzca un número entre 1 y 100")
                    guessNum : int = int(input())
                    self.juego.realizarJugada(guessNum)
                    print(self.juego.getResultado())
                if(opcion == 2):
                    print("El número de intentos máximos es: " + str(self.juego.getMaxIntentos()))
                if(opcion == 3):
                    print("Usted lleva: " + str(self.juego.getIntentos()) + " intentos")
                    print("Le quedan: " + str((self.juego.getMaxIntentos() - self.juego.getIntentos())) + " intentos")
                if(opcion == 4):
                    print("El último número que ha introducido es: " + str(self.juego.getIntentado()))
                if(opcion == 5):
                    self.juego.resetJuego()
                    print("El número secreto era " + str(self.juego.getNumeroSecreto()))
                if(opcion == 6):
                    print("Adiós, gracias por jugar")
                    print("El número secreto era " + str(self.juego.getNumeroSecreto()))
            else:
                print("Introduzca una opción válida por favor")

        sigue : chr = self.seguirJugando()
        if(sigue == 'S' and opcion != 6):
            self.juego.resetJuego()
            self.iniciar()


    '''
     Método que imprime el menú por consola
    '''
    def presentacionJuego(self) -> None:
        print("Elija una opción")
        print("1.- Introducir un número")
        print("2.- Consultar cuántos intentos tiene en total")
        print("3.- Consultar cuántos intentos lleva")
        print("4.- Consultar cuál es el último número que ha introducido")
        print("5.- Reiniciar el juego")
        print("6.- Salir del juego")

    '''
     Método que lee la opción introducida por el jugador
     @return opcion : int
    '''
    def leerNumero(self) -> int:
        self.presentacionJuego()
        opcion : int = int(input())
        return opcion

    '''
     Método que pregunta al jugador si quiere seguir jugando
     @return sigue : chr
     Si devuelve S, se reinicia el juego, si devuelve N se acaba
    '''
    def seguirJugando(self) -> chr:
        sigue : chr = ''
        while(sigue != 'S' and sigue != 'N'):
            print("¿Quiere seguir jugando?")
            print("S/N")
            entradaTeclado = input().capitalize()
            sigue = entradaTeclado[0]
        return sigue
