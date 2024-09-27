import sys

def main():
    card = get_card()
    length = len(card)
    if length not in [13, 15, 16]:
        print("INVALID")
        sys.exit(1)
    #luhn(card_to_int(card))
    if luhn(card) == False:
        print("INVALID")
        sys.exit(2)
    if length in [13, 16] and card[0] == "4":
        print("VISA")
        sys.exit(0)
    if length == 15 and card[0]+card[1] in ["34", "37"]:
        print("AMEX")
        sys.exit(0)
    if length == 16 and card[0] == "5" and 1 <= int(card[1]) <= 5:
        print("MASTERCARD")
        sys.exit(0)
    print("INVALID")
    sys.exit(3)

def luhn(card):
    i = -2
    x = 0
    y = 0
    while i >= -len(card):
        xx = 2 * int(card[i])
        for val in str(xx):
            x += int(val)
        i -= 2
    i = -1
    while i >= -len(card):
        y += int(card[i])
        i -= 2
    luhnval = x + y
    if luhnval % 10 == 0:
        return True
    return False


#def card_to_int(card):
#    i = 0
#    int_card = 0
#    for number in reversed(card):
#        int_card += int(number)*pow(10, i)
#        i += 1
#    return int_card


def get_card():
    while 1:
        card = input("Number: ").strip()
        error = False
        for num in card:
            try:
                int(num)
            except:
                error = True
        if (error == False):
            return card

if __name__ == "__main__":
    main()
