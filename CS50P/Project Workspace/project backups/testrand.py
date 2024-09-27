from projectv11continuehere import TicTacToe

def main():
    list = [1,2,3,4,5]
    obj = TicTacToe()
    for _ in range(5):
        prt = obj.random(list)
        print(prt)
        list.remove(prt)

main()
