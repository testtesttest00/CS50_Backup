def main():
    cart = {}
    while 1:
        try:
            item = newentry()
            if item in cart:
                cart.update({item : cart[item] + 1})
            else:
                cart.setdefault(item, 1)
        except EOFError:
            for item in cart:
                print(item)
                print(sortalpha(item))
            print(cart.items())
            break

def newentry():
    item = str(input()).upper().strip()
    return item

abc = "abcdefghijklmnoqrstucwxyz"
def sortalpha(text):


"""
ok here's what's wrong:
dict can form lists >> look for list methods too!

now i realised what ive done below is dumb

ok time to do a makeover.
"""





'''
abcdefhijklmnopqrstuvwxyz  -> for char in alphabet... return 1char(abc)
    list(cart) -> for key in list(cart),,, e.g. apple
        apple -> for char in key... return 1char(key)
    if 1char(key) == 1char(abc) >>store>> passed = []
    else >>store>> failed = []
    :
    :
    :
(passed = [apple, avocado...], failed = [banana, carrot, zebra...])
    :
    :
    :
----------------------- i hereby reject the above idea-----------------
VVV keys in dict
apple            1) check all key[0] with "a"    >    i == 1 if true, pass if false
aaa              2) check all key[1] with "a"    >    if true, i+=  | if i == len(key), store key (d[x]) in list
a                3) .
banana           4) .       repeat steps 1 & 2 till all i == 1 returns false
bottle           5) .
bull             6) repeat steps 1-5, changing "a"(aka abc[0]) with "b" (aka abc[1]), up to abc[25] >> list sorted
'''
main()
