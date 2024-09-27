import sys

class TicTacToe():

    def __init__(self):
        while 1:
            print("\n")
            self.player = input("Play as X or O?\n").strip().upper()
            if self.player in ["X", "O"]:
                break
            else:
                print("Only X or O are valid. Try again or press Ctrl + C to exit the game.")
        self.board = {"a1":".","a2":".","a3":".","b1":".","b2":".","b3":".","c1":".","c2":".","c3":"."}

    def __str__(self):
        return f"  A B C\n1 {self.board["a1"]} {self.board["b1"]} {self.board["c1"]}\n2 {self.board["a2"]} {self.board["b2"]} {self.board["c2"]}\n3 {self.board["a3"]} {self.board["b3"]} {self.board["c3"]}\n"

    def displaypos(self):
        position = input("\nKey in the position:\n").lower().strip()
        if position in self.board:
            print(self.board)
            print(self.board[position])
        else:
            print("Invalid")

    def start(self):
        self.turn = 1
        while 1:
            self.gamemode = input("\nChoose your gamemode:\n1) vs CPU\n2) Pass and Play\n\n").strip()
            if self.gamemode in ["1","2"]:
                break
            else:
                print("Enter 1 or 2 only.")
        if self.gamemode == "1":
            self.cpu()
        elif self.gamemode == "2":
            self.pnp()

    def cpu(self): #different difficulties? hardcoded to win and random positions
        self.cpulist = list(self.board)
        while 1:
            self.difficulty = input("\nChoose your difficulty:\n1) Easy\n2) Not Easy\n\n").strip()
            if self.difficulty in ["1", "2"]:
                break
            else:
                print("Enter 1 or 2 only.")
        if self.player == "X":
            self.ai = "O" #can use self.player2 in place of self.ai
        else:
            self.ai = "X"
        while 1:
            self.seq = int(input("\nChoose who to go first:\n1) CPU\n2) Player\n\n").strip())
            if self.seq in [1, 2]:
                break
            else:
                print("Enter 1 or 2 only.")
        self.nextmove()

    def computation(self):
        if self.difficulty == "1":
            cpunextpos = self.random(self.cpulist)
            self.cpulist.remove(cpunextpos)
            return cpunextpos

    def random(self, iterable):
        hs = list(str(hash(self)))
        finallist = list(str(round(hash(self)/(int(hs[len(hs) - 1])+1)*10, None)))[2:]
        for i in [0,8]:
            i += 1
            return iterable[(int(finallist[i - 1])+1)%len(iterable)]

    def pnp(self):
        if self.player == "X":
            self.player2 = "O"
        else:
            self.player2 = "X"
        self.nextmove()

    def nextmove(self):
        print("==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==")
        while self.turn <= 9:
            active = self.nextplayer()
            print(f"Turn {self.turn}\n{active} to move", end = "")
            print(f"\n{self}", end = "")
            self.checkwin()
            while 1:
                if self.gamemode == "2" or self.gamemode == "1" and active == self.player:
                    pos = input("\nPosition: ").strip().lower()
                elif self.gamemode == "1" and active == self.ai:
                    print("\nCPU INPUTTING...", end = "")
                    pos = self.computation()
                    print(pos)
                if pos not in self.board:
                    print("Invalid position.")
                elif self.board[pos] != ".":
                    print("Position is already filled. Choose another one.")
                elif self.board[pos] == ".":
                    self.board[pos] = active
                    if self.gamemode == "1" and pos in self.cpulist:
                        self.cpulist.remove(pos)
                    self.turn += 1
                    break
        print("No more moves to make")
        self.end()

    def nextplayer(self):
        if self.turn % 2 == 1 and self.gamemode == "2":
            active = self.player
        elif self.turn % 2 == 0 and self.gamemode == "2":
            active = self.player2
        elif self.gamemode == "1":
            if self.seq == 1 and self.turn % 2 == 1:
                active = self.ai
            elif self.seq == 1 and self.turn % 2 == 0:
                active = self.player
            elif self.seq == 2 and self.turn % 2 == 1:
                active = self.player
            elif self.seq == 2 and self.turn % 2 == 0:
                active = self.ai
        return active

    def checkwin(self): #include last placed x or o and self.end(lastplaced)? make mechanism to normalise the board e.g. a1 a2 a3 == a3 b3 c3?
        if self.board["a1"] == self.board["a2"] == self.board["a3"] or self.board["a1"] == self.board["b1"] == self.board["c1"]:
            self.end(self.board["a1"])
        elif self.board["b1"] == self.board["b2"] == self.board["b3"] or self.board["a2"] == self.board["b2"] == self.board["c2"]:
            self.end(self.board["b2"])
        elif self.board["c1"] == self.board["c2"] == self.board["c3"] or self.board["a3"] == self.board["b3"] == self.board["c3"]:
            self.end(self.board["c3"])
        elif self.board["a1"] == self.board["b2"] == self.board["c3"] or self.board["a3"] == self.board["b2"] == self.board["c1"]:
            self.end(self.board["b2"])
        else:
            pass

    def end(self, player = None): #make strikethrough on winning postions and print?
        print(player)
        print("erm wow")
        if player in ["X", "O"]:
            if self.gamemode == "1" and self.player != player:
                name = "CPU"
            elif self.gamemode == "2" and self.player != player:
                name = "Player 2"
            elif self.gamemode == "2":
                name = "Player 1"
            else:
                name = "Player"
            exit(f"{name} ({player}) wins")
#            self.turn = 10
        elif player == None:
            exit("Tie")

    @property
    def board(self):
        return self._board
    @board.setter
    def board(self, board):
        if list(board) == ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'] and isinstance(board, dict):
                 self._board = board
        else:
            pass

def main():
    print("\n\nLet's play a game of Tic-Tac-Toe!", end = "")
    ttt = TicTacToe()
    ttt.start()
#    for _ in range(256):
#        ttt_ = TicTacToe()
##        ttt_.start()
 #       game = input("Input 'Yes' to rematch\n").strip().lower()
 #       if game not in ["yes", "y"]:
 #           sys.end("See you next time.\n\n\n\n\n")

    #ttt1.board["a1"] = "asd" - how to protect from this?

if __name__ == "__main__":
    main()
