from datetime import date
import re
import sys
import inflect

class Date:

    def __init__(self, date):
        self.date = date
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, input):
        if type(input) == str:
            if re.match(r"\d{4}-\d{2}-\d{2}", input):
                self._date = date.fromisoformat(input)
            else:
                sys.exit("Invalid date")
        elif isinstance(input, date):
            self._date = input
        else:
            sys.exit(type(input))

    #@classmethod
    #def get(self):
    #    return Date(input("Birthday: ").strip())

def main():
    bday = Date(input("Date of Birth: ").strip())
    #today = Date(date.today())
    #diff = today.date - bday.date
    #print(date.isoformat(date.today()))
    diff = date.today() - bday.date
    words = inflect.engine().number_to_words(diff.days*1440, andword="")
    print(words.capitalize(), "minutes")

if __name__ == "__main__":
    main()
