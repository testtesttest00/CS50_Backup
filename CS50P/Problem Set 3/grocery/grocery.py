def newitem():
    item = str(input()).upper().strip()
    return item

def main():
    cart = {}
    while 1:
        try:
            item = newitem()
            if item in cart:
                cart.update({item : cart[item]+1})
                pass
            else:
                cart.setdefault(item, 1)
        except EOFError:
            abcitems = sorted(list(cart))
            for i in abcitems:
                print(cart[i], i)
            break
main()

"""
lines 16 - 17

abcitems = sorted(list(cart))
for i in abcitems:

^^^ yields correct results

whereas

list(cart).sort()
for i in list(cart)

^^^ sorts "tortilla" above "sweet potato" (wrong!)
"""
