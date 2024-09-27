def main():
    exp = str(input("Expression: ")).strip()
    x, y, z = exp.split()
    if y == "+":
        ans = float(x)+float(z)
    elif y == "-":
        ans = float(x)-float(z)
    elif y == "*":
        ans = float(x)*float(z)
    else:
        ans = float(x)/float(z)
    print(f"{ans:.1f}")

main()
