import csv
import sys
from sys import argv


def main():

    if len(argv) != 3:
        error(1)

    try:
        db = open(argv[1], "r")
        header = db.readline().strip("\n").split(",")
        #print(header)
        db_obj = csv.DictReader(db, header)
        #print(db_obj)
        #for person in db_obj:
        #    print(person)
    except FileNotFoundError:
        error(2)

    try:
        with open(argv[2], "r") as s:
            seq = s.read()
    except FileNotFoundError:
        error(2)

    matches = {}
    for strs in header[1:]:
        matches[strs] = str(longest_match(seq, strs))
    #print(matches)

    for person_dict in db_obj:
        match_flag = True
        for strs in matches:
            if person_dict[strs] != matches[strs]:
                match_flag = False
                break
        if match_flag:
            print(f"{person_dict["name"]}")
            break
    if match_flag == False:
        print("No match")
# In Python, a variable defined inside a loop retains its value and scope within the entire function.
# In contrast, in C, a variable defined inside a loop block would lose its scope outside that block.

    db.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

def error(error_code):
    print("Usage: python dna.py database.csv sequence.txt")
    sys.exit(error_code)

main()
