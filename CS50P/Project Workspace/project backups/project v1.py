import sys
#tic tac toe
class Board():

    positions = {"a1":"0","a2":"1","a3":"2",
                 "b1":"3","b2":"4","b3":"5",
                 "c1":"6","c2":"7","c3":"8"}

    def __init__(self, a1=".", a2=".", a3=".", b1=".", b2=".", b3=".", c1=".", c2=".", c3="."):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.template = f"\n\n_ABC\n1{self.a1}{self.a2}{self.a3}\n2{self.b1}{self.b2}{self.b3}\n3{self.c1}{self.c2}{self.c3}\n\n"
        self.liveboard=[self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3]

    def __str__(self):
        return self.template

    def inp(self):
        position = input("\nKey in the position:\n").lower().strip()
        if position in self.positions:
            print(self.liveboard[int(self.positions[position])])


    @property
    def a1(self):
        return self._a1
    @a1.setter
    def a1(self, inp):
        if inp in [".", "x", "o"]:
            self._a1 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._a1 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def a2(self):
        return self._a2
    @a2.setter
    def a2(self, inp):
        if inp in [".", "x", "o"]:
            self._a2 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._a2 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def a3(self):
        return self._a3
    @a3.setter
    def a3(self, inp):
        if inp in [".", "x", "o"]:
            self._a3 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._a3 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def b1(self):
        return self._b1
    @b1.setter
    def b1(self, inp):
        if inp in [".", "x", "o"]:
            self._b1 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._b1 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def b2(self):
        return self._b2
    @b2.setter
    def b2(self, inp):
        if inp in [".", "x", "o"]:
            self._b2 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._b2 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def b3(self):
        return self._b3
    @b3.setter
    def b3(self, inp):
        if inp in [".", "x", "o"]:
            self._b3 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._b3 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def c1(self):
        return self._c1
    @c1.setter
    def c1(self, inp):
        if inp in [".", "x", "o"]:
            self._c1 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._c1 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def c2(self):
        return self._c2
    @c2.setter
    def c2(self, inp):
        if inp in [".", "x", "o"]:
            self._c2 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._c2 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")

    @property
    def c3(self):
        return self._c3
    @c3.setter
    def c3(self, inp):
        if inp in [".", "x", "o"]:
            self._c3 = inp
        else:
            print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")
            while 1:
                inp = input("Input A1:\n").lower().strip()
                if inp in [".", "x", "o"]:
                    self._c3 = inp
                    break
                else:
                    print("\nOnly X or O are allowed.\nPress ctrl + c to end game.\n")




def main():
    ttt1 = Board()
    print(ttt1)
    ttt1.inp()

if __name__ == "__main__":
    main()
