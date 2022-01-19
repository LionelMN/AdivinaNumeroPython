from model.SecretNumberGame import SecretNumberGame

'''
 Class of the interfaz of the game
'''
class Interfaz:
    game: SecretNumberGame

    '''
     Class' constructor
     Inicializa game
    '''
    def __init__(self) -> None:
        self.game = SecretNumberGame()
        pass

    '''
     Initializes the game
     Ask the player for a correct option to play
     The game ends when the player guess the secret number, exits the game or consumes all the tries
     If the game ends asks the player if wants to play again, except when the player exits the game
    '''
    def start(self) -> None:
        option : int = 1
        while(option != 6 and self.game.getIsOver() == False and self.game.getTries() < self.game.getMaxTries()):
            option = self.leerNumero()
            if(option >= 1 and option <=6):
                if(option == 1):
                    print("Please introduce a number between 1 and 100")
                    guessNum : int = int(input())
                    self.game.play(guessNum)
                    print(self.game.getMessage())
                if(option == 2):
                    print("You have : " + str(self.game.getMaxTries()) + " tries at maximum")
                if(option == 3):
                    print("You have consumed: " + str(self.game.getTries()) + " tries")
                    print("There are : " + str((self.game.getMaxTries() - self.game.getTries())) + " tries left")
                if(option == 4):
                    print("The last number you have introduced: " + str(self.game.getTriedNumber()))
                if(option == 5):
                    self.game.resetGame()
                    print("The secret number was " + str(self.game.__getsecretNumber()))
                if(option == 6):
                    print("Goodbye, thanks for playing")
                    print("The secret number was " + str(self.game.__getsecretNumber()))
            else:
                print("Please introduce a valid option")

        keepPlaying : chr = self.keepPlaying()
        if(keepPlaying == 'S' and option != 6):
            self.game.resetGame()
            self.start()


    '''
     Prints menu
    '''
    def printMenu(self) -> None:
        print("Choose an option")
        print("1.- Introduce a number")
        print("2.- Check Max tries")
        print("3.- Check how many tries remains")
        print("4.- Check the last number introduced")
        print("5.- Reset game")
        print("6.- Exit game")

    '''
     Reads by keyboard the option
     @return opcion : int
    '''
    def leerNumero(self) -> int:
        self.printMenu()
        option : int = int(input())
        return option

    '''
     Ask the player to play again
     @return sigue : chr
     if S reset the game
    '''
    def keepPlaying(self) -> chr:
        sigue : chr = ''
        while(sigue != 'S' and sigue != 'N'):
            print("Do you want to keep playing?")
            print("S/N")
            entradaTeclado = input().capitalize()
            sigue = entradaTeclado[0]
        return sigue
