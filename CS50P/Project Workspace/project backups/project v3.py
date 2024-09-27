import sys
#tic tac toe
class TicTacToe():

    while 1:
        print("\n")
        player = input("Play as X or O?\n").strip().upper()
        if player in ["X", "O"]:
            break
        else:
            print("Only X or O are valid. Try again or press Ctrl + C to exit the game.")

    def __init__(self):
        self.boardedit = 6
        self.board = {"a1":".","a2":".","a3":".","b1":".","b2":".","b3":".","c1":".","c2":".","c3":"."}

    def __str__(self):
        return f"{list(self.board)}"

    def displaypos(self):
        position = input("\nKey in the position:\n").lower().strip()
        if position in self.board:
            print(self.board[position])
        else:
            print("Invalid")

    def start(self):
        self.turn = 1
        while 1:
            gamemode = input("\nChoose your gamemode:\n1) vs CPU\n2) Pass and Play\n\n").strip()
            if gamemode in ["1","2"]:
                break
            else:
                print("Enter 1 or 2 only.")
        if gamemode == "1":
            self.cpu()
        elif gamemode == "2":
            self.pnp()

    def cpu(self):
        self.nextmove()

    def pnp(self):
        if self.player == "X":
            self.player2 = "O"
        else:
            self.player2 = "X"
        print(f"Player 1 ({self.player})'s move")
        self.nextmove()

    def nextmove(self):
        self.boardedit = 1
        while 1:
            if self.turn <= 9:
                print(f"Turn {self.turn}")
                while 1:
                    pos = input("Position: ").strip().lower()
                    if pos not in self.board:
                        print("Invalid position.")
                    else:
                        break
                while 1:
                    if self.board[pos] == ".":
                        self.board[pos] = self.player
                        self.turn += 1
                        break
                    else:
                        print(self.board)
                        print("Position is already filled. Choose another posistion.\n")
                        self.nm()
                print(self.board)
            elif self.turn > 9:
                break
        self.end()

    def end(self):
        if 5 < self.turn <= 9:
            exit(f"{self.player} wins")
        if self.turn > 9:
            print("Tie")

    @property
    def board(self):
        if self.boardedit in [1,2,3,4,5,6]:
            self.boardedit -= 1
            return self._board
        else:
            return {}
    @board.setter
    def board(self, board):
        if list(board) == ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'] and isinstance(board, dict):
                 self._board = board
        else:
            pass

def main():
    ttt1 = TicTacToe()
    ttt1.board["a1"] = "asd"
    ttt1.start()

if __name__ == "__main__":
    main()
