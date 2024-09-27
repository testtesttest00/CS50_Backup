from validator_collection import validators, checkers, errors

def main():
    try:
        email_inp = validators.email(str(input("What's your email address? ")).strip())
        if email_inp:
            print("Valid")
    except (ValueError, errors.EmptyValueError, errors.InvalidEmailError):
        print("Invalid")

if __name__ == "__main__":
    main()

#original attempt
