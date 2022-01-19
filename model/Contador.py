'''
 Clase que simula el comportamiento de un contador
'''
class Contador:
    cuenta : int

    '''
     Constructor de la clase
     Inicializa la cuenta a 0
    '''
    def __init__(self) -> None:
        self.cuenta = 0
        pass

    '''
     Método que incrementa la cuenta en 1
    '''
    def incrementar(self) -> None:
        self.cuenta += 1

    '''
     Método que decrementa la cuenta en 1
    '''
    def decrementar(self) -> None:
        self.cuenta -= 1

    '''
     Método que devuelve la cuenta
     @return cuenta
    '''
    def getCuenta(self) -> int:
        return self.cuenta

    '''
     Método que reinicia el contador
    '''
    def reiniciarCuenta(self) -> None:
        self.cuenta = 0