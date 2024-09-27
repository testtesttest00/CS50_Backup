import sys
#tic tac toe
class Board():

    def __init__(self):
        self.liveboard = {"a1":".","a2":".","a3":".",
                         "b1":".","b2":".","b3":".",
                         "c1":".","c2":".","c3":"."}

    def __str__(self):
        return f"{list(self.liveboard)}"

    def display(self):
        position = input("\nKey in the position:\n").lower().strip()
        if position in self.liveboard:
            print(self.liveboard[position])
        else:
            print("Invalid")

    @property
    def liveboard(self):
        return self._liveboard
    @liveboard.setter
    def liveboard(self, board):
        self._liveboard = board
        # move input request out of property, make class method
        while 1:
            val = input("Input X/O: ").strip().lower()
            if val not in [".", "x", "o"]:
                 print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            else:
                break
        while 1:
            pos = input("Position: ").strip().lower()
            if pos not in self.liveboard:
                print("Invalid position.")
            else:
                break
        #move input request out but leave property setting line untouched (below)
        self._liveboard[pos] = val
        '''
        if inp in [".", "x", "o"] and pos in self.liveboard:
            self._liveboard[pos] = inp
        elif inp not in [".", "x", "o"]:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input(f"Input X/O:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._liveboard[pos] = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
        elif pos not in self.liveboard:
            print("\nInvalid position.\nPress ctrl + c to end game.\n")
            while 1:
                pos = input(f"Input position:\n").lower().strip()
                if pos in self.liveboard:
                    self._liveboard[pos] = inp
                    break
                else:
                    print("\nInvalid postion.\nPress ctrl + c to end game.\n")
        elif inp not in [".", "x", "o"] and pos not in self.liveboard:
            print("bruh")
'''
def main():
    ttt1 = Board()
    print(ttt1)
    ttt1.display()

if __name__ == "__main__":
    main()
