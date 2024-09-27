import validators

def main():
    if validators.email(str(input("What's your email? ")).strip()):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

# ValidationError(func=email, args={'value': 'value'}) was printed out and except was not raised. Use if/else.

# Other attempt
