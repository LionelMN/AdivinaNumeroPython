from random import randrange

from model.Contador import Contador

'''
 Clase que simula el comportamiento del juego de Adivinar el Número
'''
class JuegoNumeroSecreto:
    MAX_INTENTOS : int = 10

    numeroSecreto : int
    numeroIntentado : int
    intentos : Contador
    terminado : bool
    resultado : str

    '''
     Constructor de la clase JuegoNumeroSecreto
    '''
    def __init__(self) -> None:
        self.intentos = Contador()
        self.resetJuego()
        pass

    '''
     Método que reinicia el juego
     Crea un nuevo numero secreto
     Pone el número de intentos a 0
     Settea el estado de terminado a falso
    '''
    def resetJuego(self) -> None:
        self.numeroSecreto = round(randrange(100))
        self.intentos.reiniciarCuenta()
        self.terminado = False
        self.resultado = ""
        self.numeroIntentado = 0
        pass

    '''
     Método que devuelve el número de intentos que ha usado el jugador
     @return intentos.cuenta : int
    '''
    def getIntentos(self) -> int:
        return self.intentos.getCuenta()

    '''
     Método que devuelve el último número introducido por el jugador
     @return numeroIntentado : int
    '''
    def getIntentado(self) -> int:
        return self.numeroIntentado

    '''
     Método que settea un nuevo valor a numeroIntentado
     @param numero : int
    '''
    def setIntentado(self, numero : int) -> None:
        self.numeroIntentado = numero

    '''
     Método que devuelve el número de intentos máximos que tiene el jugador para adivinar el número secreto
     @return MAX_INTENTOS : int
    '''
    def getMaxIntentos(self) -> int:
        return self.MAX_INTENTOS

    '''
     Método que devuelve el número secreto
     @return numeroSecreto : int
    '''
    def getNumeroSecreto(self) -> int:
        return self.numeroSecreto

    '''
     Método que aumenta el número de intentos consumidos por el jugador
    '''
    def consumirIntento(self) -> None:
        self.intentos.incrementar()

    '''
     Método que simula una jugada
     Settea un nuevo valor a numeroIntentado y lo compara con numeroSecreto
     Si coinciden:
        · se muestra el mensaje "Enhorabuena has adivinado el número secreto"
        · se termina el juego
     Si no:
        · se consume un intento
        · se compara enumeroIntentado con numeroSecreto
         Si es mayor:
            · se muestra el mensaje "Más bajo"
         Si es menor:
            · se muestra el mensaje "Más alto"
    '''
    def realizarJugada(self, numero : int) -> None:
        self.setIntentado(numero)
        if(self.getIntentado() == self.getNumeroSecreto()):
            self.resultado = "Enhorabuena has adivinado el número secreto"
            self.terminado = True
        else:
            self.consumirIntento()
            if(self.getIntentado() > self.getNumeroSecreto()):
                self.resultado = "Más bajo"
            else:
                self.resultado = "Más alto"

    '''
     Método que devuelve el estado del juego
     @return terminado : bool
    '''
    def haTerminado(self) -> bool:
        return self.terminado

    '''
     Método que devuelve el mensaje resultado de realizar una jugada
     @return resultado : str
    '''
    def getResultado(self) -> str:
        return self.resultado
