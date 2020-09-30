class PaperRockScissors:

    def start  (self):
        print("Hi Player 1 choose your move:")
        print("1- Paper")
        print("2- Rock")
        print("3- Scissors")
        firstMove = self.getInput()
        if self.inputComprover(firstMove)==True:
            return self.secondMove(firstMove)

    def getInput (self):
        move=int(input())
        return move

    def secondMove (self, firstMove):
        print("Hi Player 2 choose your move:")
        print("1- Paper")
        print("2- Rock")
        print("3- Scissors")
        secondMove=self.getInput()
        if self.inputComprover(secondMove)==True:
            return self.winnerComprover(firstMove,secondMove)

    def inputComprover (self, move):
        if isinstance(move, str) == True:
            print('Introduce sólo números!')
            return False
        if move > 3 or move < 1:
            print('Introduce sólo números válidos!')
            return False
        return True
    
    def winnerComprover (self, firstMove, secondMove):
        if firstMove == secondMove :
            message="Empate"
            return message
        if firstMove == 1 and secondMove == 2:
            message="Player 1 wins"
            return message
        if firstMove == 2 and secondMove == 3:
            message="Player 1 wins"
            return message
        if firstMove == 3 and secondMove == 1:
            message="Player 1 wins"
            return message
        message="Player 2 wins"
        return message