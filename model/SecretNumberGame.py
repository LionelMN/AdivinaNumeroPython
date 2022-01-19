from random import randrange

from model.Counter import Counter

'''
 Clase that simulates the behaviour of a guess the number game
'''
class SecretNumberGame:
    MAX_TRIES : int = 10
    secretNumber : int
    triedNumber : int
    tries : Counter
    isOver : bool
    resultado : str

    '''
     SecretNumberGame's constructor
    '''
    def __init__(self) -> None:
        self.tries = Counter()
        self.resetGame()
        pass

    '''
     Resets the game
     Creates a new secretNumber
     Sets tries to 0
     Sets isOver to False
    '''
    def resetGame(self) -> None:
        self.secretNumber = round(randrange(100))
        self.tries.resetCount()
        self.isOver = False
        self.message = ""
        self.triedNumber = 0
        pass

    '''
     Getter of tries
     @return tries.cuenta : int
    '''
    def getTries(self) -> int:
        return self.tries.getCount()

    '''
     Getter of triedNumber
     The last number introduced by the player
     @return triedNumber : int
    '''
    def getTriedNumber(self) -> int:
        return self.triedNumber

    '''
     Setter of triedNumber
     @param number : int
    '''
    def setTriedNumber(self, number : int) -> None:
        self.triedNumber = number

    '''
     Getter of MAX_TRIES
     @return MAX_TRIES : int
    '''
    def getMaxTries(self) -> int:
        return self.MAX_TRIES

    '''
     Getter of secretNumber
     @return secretNumber : int
    '''
    def __getsecretNumber(self) -> int:
        return self.secretNumber

    '''
     Increases the number of tries when the player introduces a number
    '''
    def increasesTries(self) -> None:
        self.tries.increment()

    '''
     Simulates a play
     Sets a new TriedNumber and compares it with secretNumber
     if it matches:
        · shows the following message "Congratulations! You guessed the secret number"
        · game overs
     else
        · Increases tries
        · compares TriedNumber with secretNumber
         If it is bigger:
            · shows the following message "Is a shorter number"
         else:
            · shows the following message "Is a larger number"
    '''
    def play(self, number : int) -> None:
        self.setTriedNumber(number)
        if(self.getTriedNumber() == self.__getsecretNumber()):
            self.message = "Congratulations! You guessed the secret number"
            self.isOver = True
        else:
            self.increasesTries()
            if(self.getTriedNumber() > self.__getsecretNumber()):
                self.message = "Is a shorter number"
            else:
                self.message = "Is a larger number"

    '''
     Getter of isOver
     @return isOver : bool
    '''
    def getIsOver(self) -> bool:
        return self.isOver

    '''
     Getter of message
     @return message : str
    '''
    def getMessage(self) -> str:
        return self.message
