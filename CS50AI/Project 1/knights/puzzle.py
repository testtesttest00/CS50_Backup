from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Given A cannot be both a Knight and a Knave
    Biconditional(AKnight, Not(AKnave)),

    # A is a Knight if "A is a Knight and a Knave" is true
    # Deduces Not(AKnight) by denying the consequent
    Implication(AKnight, And(AKnight, AKnave)),

    # A is a Knave if "A is a Knight and a Knave" is false
    # Can be removed as antecedent cannot be proven by accepting the consequent
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Given A and B can only be a Knight or a Knave
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # Both A and B are Knaves if A is a Knight
    # Deduces that Not(AKnight) by denying the consequent
    Implication(AKnight, And(AKnave, BKnave)),

    # A and B are not both Knaves if A is a Knave
    # Deduces that Not(BKnave) by accepting the antecedent
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Given A and B can only be a Knight or a Knave
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),

    # If A is a Knight
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    # If A is a Knave
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),

    # If B is a Knight
    Implication(BKnight, Biconditional(AKnight, BKnave)),
    # If B is a Knave
    Implication(BKnave, Not(Biconditional(AKnight, BKnave)))
)


eitheror = And(
    # Given A, B and C can only be a Knight or a Knave
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave))
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Given A, B and C can only be a Knight or a Knave
    eitheror,


    # Deduces AKnight since only statement 1 is possible (the other 3 will result in AKnight & AKnave which is denied by eitheror)
    # If A is a Knight and says A is a Knight, A is a Knight
    Implication(Biconditional(AKnight, AKnight), AKnight),
    # If A is a Knight and says A is a Knave, A is a Knight that also becomes a Knave
    Implication(Biconditional(AKnight, AKnave), AKnave),
    # If A is a Knave and says A is a Knight, A is a Knave
    Implication(Biconditional(AKnave, AKnight), AKnave),
    # If A is a Knave and says A is a Knave, A is a Knave that also becomes a Knight
    Implication(Biconditional(AKnave, AKnave), AKnight),


    # Deduces BKnave since A cannot be a Knight or Knave saying he is a Knave, and since CKnight is known, denying consequent
    # If B is a Knight, either A is a Knight or a Knave claiming to be a Knave and C is a Knave
    Implication(BKnight, And(Biconditional(And(AKnight, AKnave), Not(And(AKnave, AKnave))), CKnave)),
    # If B is a Knave, A is neither a Knight nor a Knave claiming to be a Knave and C is not a Knave
    # Can be removed as antecedent cannot be proven by accepting the consequent
    Implication(BKnave, Not(And(Biconditional(And(AKnight, AKnave), Not(And(AKnave, AKnave))), CKnave))),


    # Deduces CKnight since AKnight is known, denying Not(AKnight) to conclude Not(CKnave)
    # If C is a Knight, A is a Knight
    # Can be removed as antecedent cannot be proven by accepting the consequent
    Implication(CKnight, AKnight),
    # If C is a Knave, A is not a Knight
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
