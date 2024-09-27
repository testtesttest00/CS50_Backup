import sys
import re
import random

class TicTacToe():

    def __init__(self, cheats):
        print(f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
        while 1:
            self.player = input("Play as X or O?\n\n").strip().upper()
            if self.player in ["X", "O"]:
                break
            else:
                print("Only X or O are valid. Try again or press Ctrl + C to exit the game.\n")
        self._board = {"a1":".","a2":".","a3":".","b1":".","b2":".","b3":".","c1":".","c2":".","c3":"."}
        self.saveboard()
        self.cheats = cheats

    def __str__(self, winningpos = []):
        for pos in winningpos:
            self.board[pos] = f"\033[4m\033[1m{self.board[str(pos)]}\033[0m"
        return f"  A B C\n\
1 {self.board["a1"]} {self.board["b1"]} {self.board["c1"]}\n\
2 {self.board["a2"]} {self.board["b2"]} {self.board["c2"]}\n\
3 {self.board["a3"]} {self.board["b3"]} {self.board["c3"]}\n"

    def displaypos(self):
        pos = input("\nKey in the position:\n").lower().strip()
        if pos in self.board:
            print(self.board)
            print(self.board[pos])
        else:
            print("Invalid")

    def saveboard(self):
        self.tempsave = self.board

    def checksetter(self):
        self.board = self.tempsave

    def start(self):
        self.checksetter()
        print(f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
        self.turn = 1
        self.lastmove = False
        while 1:
            self.gamemode = input("Choose your gamemode:\n1) vs CPU\n2) Pass and Play\n\n").strip()
            if self.gamemode in ["1","2"]:
                break
            else:
                print("Enter 1 or 2 only.\n")
        if self.gamemode == "1":
            self.cpu()
        elif self.gamemode == "2":
            self.pnp()

    def cpu(self):
        print(f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
        self.cpulist = list(self.board)
        while 1:
            self.difficulty = input("Choose your difficulty:\n1) Easy\n2) Easy++\n\n").strip()
            if self.difficulty in ["1", "2"]:
                break
            else:
                print("Enter 1 or 2 only.\n")
        if self.player == "X":
            self.ai = "O"
        else:
            self.ai = "X"
        print(f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
        while 1:
            self.seq = input("Choose who to go first:\n1) CPU\n2) Player\n\n").strip()
            if self.seq in ["1", "2"]:
                break
            else:
                print("Enter 1 or 2 only.\n")
        self.nextmove()

    def computation(self):
        if self.difficulty == "1":
            cpunextpos = self.random(self.cpulist)
            self.cpulist.remove(cpunextpos)
            return cpunextpos
        elif self.difficulty == "2":
            cpunextpos = self.tttcalculator(list(self.board.values()))
            self.cpulist.remove(cpunextpos)
            return cpunextpos

    def random(self, iterable):
        try:
            if self.rlist:
                for num in self.rlist:
                    self.rlist.remove(num)
                    return iterable[(int(num)+1)%len(iterable)]
        except AttributeError:
            hs = list(str(hash(self)))
            self.rlist = list(str(round(hash(self)/(int(hs[len(hs) - 1])+1)*10, None)))[:7]
            num = self.rlist[0]
            self.rlist.remove(num)
            return iterable[(int(num)+1)%len(iterable)]

    def tttcalculator(self, current):
        if (self.ai==current[1]==current[2] or
            self.ai==current[3]==current[6] or
            self.ai==current[4]==current[8]) and current[0] == ".":
            return "a1"
        elif (self.ai==current[0]==current[2] or
              self.ai==current[4]==current[7]) and current[1] == ".":
            return "a2"
        elif (self.ai==current[0]==current[1] or
              self.ai==current[4]==current[6] or
              self.ai==current[5]==current[8]) and current[2] == ".":
            return "a3"
        elif (self.ai==current[4]==current[5] or
              self.ai==current[0]==current[6]) and current[3] == ".":
            return "b1"
        elif (self.ai==current[3]==current[5] or
              self.ai==current[1]==current[7] or
              self.ai==current[0]==current[8] or
              self.ai==current[2]==current[6]) and current[4] == ".":
            return "b2"
        elif (self.ai==current[3]==current[4] or
              self.ai==current[2]==current[8]) and current[5] == ".":
            return "b3"
        elif (self.ai==current[7]==current[8] or
              self.ai==current[0]==current[3] or
              self.ai==current[2]==current[4]) and current[6] == ".":
            return "c1"
        elif (self.ai==current[6]==current[8] or
              self.ai==current[1]==current[4]) and current[7] == ".":
            return "c2"
        elif (self.ai==current[6]==current[7] or
              self.ai==current[2]==current[5] or
              self.ai==current[0]==current[4]) and current[8] == ".":
            return "c3"
        elif (self.player==current[1]==current[2] or
              self.player==current[3]==current[6] or
              self.player==current[4]==current[8]) and current[0] == ".":
            return "a1"
        elif (self.player==current[0]==current[2] or
              self.player==current[4]==current[7]) and current[1] == ".":
            return "a2"
        elif (self.player==current[0]==current[1] or
              self.player==current[4]==current[6] or
              self.player==current[5]==current[8]) and current[2] == ".":
            return "a3"
        elif (self.player==current[4]==current[5] or
              self.player==current[0]==current[6]) and current[3] == ".":
            return "b1"
        elif (self.player==current[3]==current[5] or
              self.player==current[1]==current[7] or
              self.player==current[0]==current[8] or
              self.player==current[2]==current[6]) and current[4] == ".":
            return "b2"
        elif (self.player==current[3]==current[4] or
              self.player==current[2]==current[8]) and current[5] == ".":
            return "b3"
        elif (self.player==current[7]==current[8] or
              self.player==current[0]==current[3] or
              self.player==current[2]==current[4]) and current[6] == ".":
            return "c1"
        elif (self.player==current[6]==current[8] or
              self.player==current[1]==current[4]) and current[7] == ".":
            return "c2"
        elif (self.player==current[6]==current[7] or
              self.player==current[2]==current[5] or
              self.player==current[0]==current[4]) and current[8] == ".":
            return "c3"
        elif self.ttthardcode(current):
            return self.ttthardcode(current)
        else:
            return self.random(self.cpulist)

    def ttthardcode(self, current):
        if self.seq == "1":
            if current[4] != self.ai:
                return "b2"
            elif current[4] == self.ai and self.player in [current[1], current[3], current[5], current[7]]:
                if current[0] == ".":
                    return "a1"
                elif self.player == current[1] and "c1" in self.cpulist:
                    return "c1"
                elif self.player == current[3] and "a3" in self.cpulist:
                    return "a3"
            elif current[4] == self.ai:
                if self.player in [current[0], current[6]] and "b3" in self.cpulist:
                    return "b3"
                elif self.player in [current[2], current[8]] and "b1" in self.cpulist:
                    return "b1"
            else:
                pass
        elif self.seq == "2":
            if self.turn == 2:
                self.switch = None
            if self.turn == 2 and current[4] == self.player and "a1" in self.cpulist:
                return "a1"
            elif self.player in [current[0], current[2], current[6], current[8]] and self.switch in[None, "Corner"]:
                if current[4] != self.ai:
                    self.switch = "Corner"
                    return "b2"
                elif self.player == current[0] == current[5] and current[7] != self.ai:
                    self.switch = "Corner"
                    return "c2"
                elif self.player == current[0] == current[7] and current[5] != self.ai:
                    self.switch = "Corner"
                    return "b3"
                elif self.player == current[2] == current[3] and current[7] != self.ai:
                    self.switch = "Corner"
                    return "c2"
                elif self.player == current[2] == current[7] and current[3] != self.ai:
                    self.switch = "Corner"
                    return "b1"
                elif self.player == current[6] == current[1] and current[5] != self.ai:
                    self.switch = "Corner"
                    return "b3"
                elif self.player == current[6] == current[5] and current[1] != self.ai:
                    self.switch = "Corner"
                    return "a2"
                elif self.player == current[8] == current[1] and current[3] != self.ai:
                    self.switch = "Corner"
                    return "b1"
                elif self.player == current[8] == current[3] and current[1] != self.ai:
                    self.switch = "Corner"
                    return "a2"
                elif self.player == current[0] == current[8] or\
                self.player == current[2] == current[6] and current[5] != self.ai:
                    self.switch = "Corner"
                    return "b3"
            elif self.player in [current[1], current[3], current[5], current[7]] and self.switch in [None, "Edge"]:
                if current[4] != self.ai:
                    self.switch = "Edge"
                    return "b2"
                elif self.player == current[1] == current[7] or\
                self.player == current[3] == current[5] and current[0] != self.ai:
                    self.switch = "Edge"
                    return "a1"
                elif self.player == current[1] == current[3] and current[0] != self.ai:
                    self.switch = "Edge"
                    return "a1"
                elif self.player == current[1] == current[5] and current[2] != self.ai:
                    self.switch = "Edge"
                    return "a3"
                elif self.player == current[3] == current[7] and current[6] != self.ai:
                    self.switch = "Edge"
                    return "c1"
                elif self.player == current[5] == current[7] and current[8] != self.ai:
                    self.switch = "Edge"
                    return "c3"
                elif self.player == current[1] == current[8] or\
                self.player == current[0] == current[5] and current[2] != self.ai:
                    self.switch = "Edge"
                    return "a3"
                elif self.player == current[2] == current[7] or\
                self.player == current[5] == current[6] and current[8] != self.ai:
                    self.switch = "Edge"
                    return "c3"
                elif self.player == current[0] == current[7] or\
                self.player == current[3] == current[8] and current[6] != self.ai:
                    self.switch = "Edge"
                    return "c1"
                elif self.player == current[1] == current[6] or\
                self.player == current[2] == current[3] and current[0] != self.ai:
                    self.switch = "Edge"
                    return "a1"
            else:
                pass
        else:
            pass

    def pnp(self):
        if self.player == "X":
            self.player2 = "O"
        else:
            self.player2 = "X"
        self.nextmove()

    def nextmove(self):
        print(f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==")
        self.checksetter()
        active = self.nextplayer()
        if active == "X":
            inactive = "O"
        else:
            inactive = "X"
        self.checkwin(inactive)
        if self.cheats == True:
            x = random.choice([1,2,3])
            if self.gamemode == "1":
                if x == 1:
                    print("CPU needs a rest")
                elif x == 2:
                    print("CPU does not feel like playing")
                elif x == 3:
                    print("CPU was unplugged")
            elif self.gamemode == "2" and self.turn > 1:
                if x == 1:
                    print("Player 2 loses a turn")
                elif x == 2:
                    print("Player 2 inputted too late")
                elif x == 3:
                    print("Player 2 was too slow")
            self.checkwin(active)
        if self.turn <= 9 and not self.lastmove:
            print(f"\nTurn {self.turn}\n{active} to move", end = "")
            print(f"\n{self}", end = "")
            self.checksetter()
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
                    self.board.update({pos:active})
                    self.saveboard()
                    if self.gamemode == "1" and pos in self.cpulist:
                        self.cpulist.remove(pos)
                    self.turn += 1
                    break
            self.checksetter()
            self.nextmove()
        elif self.turn > 9 and not self.lastmove:
            print("\nNo more moves to make\n")
            self.end()

    def nextplayer(self):
        if self.turn % 2 == 1 and self.gamemode == "2":
            active = self.player
        elif self.turn % 2 == 0 and self.gamemode == "2":
            active = self.player2
        elif self.gamemode == "1":
            if self.seq == "1" and self.turn % 2 == 1:
                active = self.ai
            elif self.seq == "1" and self.turn % 2 == 0:
                active = self.player
            elif self.seq == "2" and self.turn % 2 == 1:
                active = self.player
            elif self.seq == "2" and self.turn % 2 == 0:
                active = self.ai
        if self.cheats == True:
            active = self.player
        return active

    def checkwin(self, lastplaced = None):
        if lastplaced == self.board["a1"] == self.board["a2"] == self.board["a3"]:
            self.end(self.board["a1"], ["a1", "a2", "a3"])
        elif lastplaced == self.board["a1"] == self.board["b1"] == self.board["c1"]:
            self.end(self.board["a1"], ["a1", "b1", "c1"])
        elif lastplaced == self.board["b1"] == self.board["b2"] == self.board["b3"]:
            self.end(self.board["b2"], ["b1", "b2", "b3"])
        elif lastplaced == self.board["a2"] == self.board["b2"] == self.board["c2"]:
            self.end(self.board["b2"], ["a2", "b2", "c2"])
        elif lastplaced == self.board["c1"] == self.board["c2"] == self.board["c3"]:
            self.end(self.board["c3"], ["c1", "c2", "c3"])
        elif lastplaced == self.board["a3"] == self.board["b3"] == self.board["c3"]:
            self.end(self.board["c3"], ["a3", "b3", "c3"])
        elif lastplaced == self.board["a1"] == self.board["b2"] == self.board["c3"]:
            self.end(self.board["b2"], ["a1", "b2", "c3"])
        elif lastplaced == self.board["a3"] == self.board["b2"] == self.board["c1"]:
            self.end(self.board["b2"], ["a3", "b2", "c1"])

    def end(self, player = None, winningpos = None):
        self.checksetter()
        if player in ["X", "O"]:
            if self.gamemode == "1" and self.player != player:
                name = "CPU"
            elif self.gamemode == "2" and self.player != player:
                name = "Player 2"
            elif self.gamemode == "2":
                name = "Player 1"
            else:
                name = "Player"
            print(f"\n{name} ({player}) wins\n")
            print(self.__str__(winningpos), end = "")
            self.winner = name
            self.lastmove = True
        elif player == None:
            print(self, end = "")
            print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
            print("Tie")
            self.winner = None
            self.lastmove = True

    def newgame(self):
        print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
        prompt = input("Type 'Yes' to start a new game\n\n").strip().lower()
        if prompt in ["yes", "y"]:
            ttt = TicTacToe()
            ttt.start()
        else:
            print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")
            print("See you next time")
            print("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n")

    @property
    def board(self):
        return self._board
    @board.setter
    def board(self, board):
        if list(board) == ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'] and isinstance(board, dict):
            for value in board.values():
                if value in ["X", "O", "."]:
                    pass
                else:
                    print(self)
                    raise Exception("Board has invalid value")
            self._board = board
        else:
            print(self)
            raise Exception("Invalid board")

#class Connect4(): #6rows7columns
#    ...
class SPS(): #scissors paper stone
    ...

class ScoreSheet():

    def __init__(self):
        self.tttscore = 0
        self.tttp1score = 0
        self.tttp2score = 0
        self.tttgames = 0
        self.tttvsgames = 0
#        self.c4games = 0
#        self.c4score = 0

    def __str__(self):
        if self.tttgames > 0:
            tttcpu = f"Tic-Tac-Toe vs CPU Score:\n\
{self.tttscore} win(s) / {self.tttgames} round(s)\n\n"
        else:
            tttcpu = ""
        if self.tttvsgames > 0:
            tttvs = f"Tic-Tac-Toe Versus Score:\n\
Player 1: {self.tttp1score} win(s) / {self.tttvsgames} round(s)\n\
Player 2: {self.tttp2score} win(s) / {self.tttvsgames} round(s)\n\n"
        else:
            tttvs = ""
        return f"\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n\n\
{tttcpu}\
{tttvs}\
==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n"

    def input(self, results):
        if inp := re.match(r"1, (\d), (.+)", results):
            mode = inp.group(1)
            winner = inp.group(2)
            if mode == "1":
                self.tttgames += 1
                if winner == "Player":
                    self.tttscore += 1
            elif mode == "2":
                self.tttvsgames += 1
                if winner == "Player 1":
                    self.tttp1score += 1
                elif winner == "Player 2":
                    self.tttp2score += 1
#        elif inp := re.match(r"2, (.+)", results):
#            winner = inp.group(1)
#            self.c4games += 1
#            if winner == "Player":
#                self.c4score += 1

def main():
    if len(sys.argv) != 2:
        password = welcome()
        cheats = secret(password)
    elif len(sys.argv) == 2:
        cheats = secret(sys.argv[1])
    score = ScoreSheet()
    while 1:
        result = startgame(cheats)
        score.input(result)
        if input("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n\n\
Play again?\n\n").lower().strip() in ["yes", "y"]:
            pass
        else:
            break
    print(score)
    #Your 3 required custom functions other than main must also be in project.py and defined
    #at the same indentation level as main (i.e., not nested under any classes or functions).

def startgame(cheats = False):
    while 1:
        start = input("\n==-==-==-=-==-==-==-==-==-==-==-==-==-==-==-==\n\n\
Select a game to play:\n\n1) Tic-Tac-Toe\n\n2) Scissors Paper Stone\n\n").lower().strip()
        if start in ["1", "tictactoe", "ttt"]:
                ttt = TicTacToe(cheats)
                ttt.start()
                if ttt.gamemode == "1":
                    return f"1, 1, {ttt.winner}"
                elif ttt.gamemode == "2":
                    return f"1, 2, {ttt.winner}"
        else:
            print("\nEnter 1 or 2 Only")
#    elif start in ["2", "connectfour", "connect4", "c4"]:
#        c4 = Connect4()
#        c4.start()
#        return f"{c4.winner}"

def welcome():
    print("\nWel\
\033[1mc\033[0m\
ome to my project!\n\
\033[1mH\033[0m\
er\
\033[1me\033[0m \
you c\
\033[1ma\033[0m\
n play games and have fun!\n\
\033[1mT\033[0m\
hank you!\n")
    password = input("Press 'Enter' to continue\n").lower().strip()
    return password

def secret(password = None):
    global cheats
    if re.match("cheat", password, re.IGNORECASE):
        cheats = True
    else:
        cheats = False
    return cheats

if __name__ == "__main__":
    main()
