import sys
from sys import argv
import requests

def main():
    if len(argv) == 2:
        try:
            n = float(argv[1])
        except (ValueError):
            sys.exit("Command-line argument is not a number")
        except (IndexError):
            raise Exception("Error!")
    try:
        btc = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
        rate = float((((btc["bpi"])["USD"])["rate"]).replace(",", ""))
        print(f"${n*rate:,.4f}")
    except (requests.RequestException):
        raise Exception("Error!")
    except UnboundLocalError:
        sys.exit("Missing command-line argument")

main()
