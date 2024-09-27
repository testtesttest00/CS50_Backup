class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        #if self.size == 0:
        #    return "None"
        #else:
            return self.size*"🍪"

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, jarsize):
        if int(jarsize) >= 0:
            self._capacity = int(jarsize)
        else:
            raise ValueError

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, cookies = 0):
        if cookies > self.capacity or cookies < 0:
            raise ValueError("Too many/little cookies!")
        else:
            self._size = cookies

def main():
    jar = Jar(input("\nJar Capacity: ").strip())
    print("Leftover cookies:", addsubtract(jar))

def addsubtract(jarobj):
    j = 1
    while 1:
        change = int(input(j*"\n+/-n to add/eat n cookies\n0 to stop adding/eating\n").strip())
        j = 0
        if change != 0:
            jarobj.size = jarobj.size + change
            print(jarobj)
        elif change == 0:
            break
    return jarobj

if __name__ == "__main__":
    main()
