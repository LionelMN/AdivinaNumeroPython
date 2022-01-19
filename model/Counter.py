'''
 Class that simulates the behaviour of a counter
'''
class Counter:
    count : int

    '''
     Class constructor
     Initialize count to 0
    '''
    def __init__(self) -> None:
        self.count = 0
        pass

    '''
     Increments count by 1
    '''
    def increment(self) -> None:
        self.count += 1

    '''
     Decrease count by 1
    '''
    def decrement(self) -> None:
        self.count -= 1

    '''
     Getter of count
     @return count
    '''
    def getCount(self) -> int:
        return self.count

    '''
     Resets count
    '''
    def resetCount(self) -> None:
        self.count = 0