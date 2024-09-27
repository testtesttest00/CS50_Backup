class Hexadecimal():
    def __init__(self, dec=0):
        self.dec = dec
    def __str__(self):
        return str(f"Decimal Form:{self.dec}")

    @property
    def dec(self):
        return self._dec
    @dec.setter
    def dec(self, dec=0):
        while 1:
            dec = input("\n\n\n\n\n\n\nInput decimal form\n").strip()
            try:
                self._dec=float(dec)
                break
            except ValueError:
                print("Input valid decimal")
                pass

def main():
    hdec_convert = Hexadecimal()
    print(f"\n{hdec_convert}")

if __name__ == "__main__":
    main()

'''
goal: make encryptor and convertor (?is that what its called?)
backup: tik-tak-toe lmao
edit: its called tic tac toe LMAO
'''
