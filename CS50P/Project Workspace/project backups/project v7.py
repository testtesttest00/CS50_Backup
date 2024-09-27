import sys

class TicTacToe():

    def __init__(self):
        while 1:
            print("\n")
            self.player = input("Play as X or O?\n\n").strip().upper()
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
            self.difficulty = input("\nChoose your difficulty:\n1) Easy\n2) Easy++\n\n").strip()
            if self.difficulty in ["1", "2"]:
                break
            else:
                print("Enter 1 or 2 only.")
        if self.player == "X":
            self.ai = "O" #can use self.player2 in place of self.ai
        else:
            self.ai = "X"
#        while 1:
#            try:
#                self.seq = int(input("\nChoose who to go first:\n1) CPU\n2) Player\n\n").strip())
#                if self.seq in [1, 2]:
#                    break
#                else:
#                    print("Enter 1 or 2 only.")
#            except ValueError:
#               print("Enter 1 or 2 only.")
#                pass
        while 1:
            self.seq = input("\nChoose who to go first:\n1) CPU\n2) Player\n\n").strip()
            if self.seq in ["1", "2"]:
                self.seq = int(self.seq)
                break
            else:
                print("Enter 1 or 2 only.")
        self.nextmove()

    def computation(self):
        if self.difficulty == "1":
            cpunextpos = self.random(self.cpulist)
            self.cpulist.remove(cpunextpos)
            return cpunextpos
        elif self.difficulty == "2":
            cpunextpos = self.tttcalculator(list(self.board.values()))
            print(cpunextpos)
            self.cpulist.remove(cpunextpos)
            return cpunextpos

    def random(self, iterable):
        hs = list(str(hash(self)))
        finallist = list(str(round(hash(self)/(int(hs[len(hs) - 1])+1)*10, None)))[2:]
        return iterable[(len(iterable)%(int(finallist[self.num()])+1))%len(iterable)]

    def num(self):
        numlist = [0,1,2,3,4,5,6,7,8]
        num = numlist[0]
        numlist.remove(num)
        return num

    def tttcalculator(self, current):
        print("\n", current, sep="")
        print(self.cpulist)
        if (self.ai==current[1]==current[2] or self.ai==current[3]==current[6] or self.ai==current[4]==current[8]) and current[0] == ".":
            return "a1"
        elif (self.ai==current[0]==current[2] or self.ai==current[4]==current[7]) and current[1] == ".":
            return "a2"
        elif (self.ai==current[0]==current[1] or self.ai==current[4]==current[6] or self.ai==current[5]==current[8]) and current[2] == ".":
            return "a3"
        elif (self.ai==current[4]==current[5] or self.ai==current[0]==current[6]) and current[3] == ".":
            return "b1"
        elif (self.ai==current[3]==current[5] or self.ai==current[1]==current[7] or self.ai==current[0]==current[8] or self.ai==current[2]==current[6]) and current[4] == ".":
            return "b2"
        elif (self.ai==current[3]==current[4] or self.ai==current[2]==current[8]) and current[5] == ".":
            return "b3"
        elif (self.ai==current[7]==current[8] or self.ai==current[0]==current[3] or self.ai==current[2]==current[4]) and current[6] == ".":
            return "c1"
        elif (self.ai==current[6]==current[8] or self.ai==current[1]==current[4]) and current[7] == ".":
            return "c2"
        elif (self.ai==current[6]==current[7] or self.ai==current[2]==current[5] or self.ai==current[0]==current[4]) and current[8] == ".":
            return "c3"
        elif (self.player==current[1]==current[2] or self.player==current[3]==current[6] or self.player==current[4]==current[8]) and current[0] == ".":
            return "a1"
        elif (self.player==current[0]==current[2] or self.player==current[4]==current[7]) and current[1] == ".":
            return "a2"
        elif (self.player==current[0]==current[1] or self.player==current[4]==current[6] or self.player==current[5]==current[8]) and current[2] == ".":
            return "a3"
        elif (self.player==current[4]==current[5] or self.player==current[0]==current[6]) and current[3] == ".":
            return "b1"
        elif (self.player==current[3]==current[5] or self.player==current[1]==current[7] or self.player==current[0]==current[8] or self.player==current[2]==current[6]) and current[4] == ".":
            return "b2"
        elif (self.player==current[3]==current[4] or self.player==current[2]==current[8]) and current[5] == ".":
            return "b3"
        elif (self.player==current[7]==current[8] or self.player==current[0]==current[3] or self.player==current[2]==current[4]) and current[6] == ".":
            return "c1"
        elif (self.player==current[6]==current[8] or self.player==current[1]==current[4]) and current[7] == ".":
            return "c2"
        elif (self.player==current[6]==current[7] or self.player==current[2]==current[5] or self.player==current[0]==current[4]) and current[8] == ".":
            return "c3"
        elif self.methods(current):
            return self.methods(current)
        else:
            return self.random(self.cpulist)

    def methods(self, current):
        if current[4] == ".":
            return "b2"
        elif current[4] != "." and current[0] == ".":
            print("passed1")
            return "a1"
        elif current[4] != "." and current[2] == ".":
            print("passed2")
            return "a3"
        elif current[4] != "." and current[6] == ".":
            print("passed3")
            return "c1"
        elif current[4] != "." and current[8] == ".":
            print("passed4")
            return "c3"
        else:
            pass

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
                    print(pos.upper())
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
        #list = [a1,a2,a3,a4,b1,b2,b3,c1,c2,c3]
        #list[0] == list[2] == list[6] == list[8]           int % 2 == 0 & int != 4
        #list[1] == list[3] == list[5] == list[7]           int % 2 == 1
        #list[4]                                            int == 4
        # a1 b1 c1 | 0  3  6     ,Observations:
        # a2 b2 c2 | 1  4  7     ,No lines of reflection
        # a3 b3 c3 | 2  5  8     ,Chart for x-4
        #Relative to C:          ,-4 -1  2     (x1 - 4  = -(x2 - 4))
        #U = Up                  ,-3  0  3     (x1 + x2 = 8)
        #D = Down                ,-2  1  4
        #L = Left                ,if placed on 8, move to 0
        #R = Right               ,if placed on 7, move to 1
        #                        ,if placed on 6, move to 2
        #                        ,if placed on 5, move to 3
        #                        ,if placed on 4, stay at 4
        #                        ,if placed on 3, move to 5
        #                        ,if placed on 2, move to 6
        #                        ,if placed on 1, move to 7
        #                        ,if placed on 0, move to 8
        #                        ,
        #                        ,create new board?
        #                        ,0 1 6 |x-4>>  -4 -3  2  symmetry on 0-4-8
        #                        ,3 4 7 |board  -1  0  3
        #                        ,2 5 8 |>>>>>  -2  1  4
        #                        ,
        # not worth to do this cool

    def end(self, player = None): #make strikethrough on winning postions and print?
        #print(self) cant do here as self.end is used every turn with player = "."
        if player in ["X", "O"]:
            #print(self)
            if self.gamemode == "1" and self.player != player:
                name = "CPU"
            elif self.gamemode == "2" and self.player != player:
                name = "Player 2"
            elif self.gamemode == "2":
                name = "Player 1"
            else:
                name = "Player"
            print(f"{name} ({player}) wins")
            self.newgame()
#            self.turn = 10
        elif player == None:
            print(self)
            print("Tie")
            self.newgame()

    def newgame(self):
        prompt = input("\nType 'Yes' to start a new game\n").strip().lower()
        if prompt in ["yes", "y"]:
            ttt_ = TicTacToe()
            ttt_.start()
        else:
            sys.exit("\nSee you next time\n")

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
