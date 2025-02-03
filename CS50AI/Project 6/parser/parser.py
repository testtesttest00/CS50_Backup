import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
NP -> N | AP NP | Det NP | NP Conj NP | NP P NP | NP VP
AP -> Adj | AP AP | AP Conj AP
VP -> V | VP NP | Adv VP | VP Conj VP | VP P NP | VP Conj NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sentence = sentence.lower()
    for char in sentence:
        if not char.isalpha():
            sentence = sentence.replace(char, " ", -1)
    processed = nltk.NLTKWordTokenizer().tokenize(sentence)
    return processed


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # original testing
    #
    # chunks = []
    #
    # subtrees = tree.subtrees(filter = lambda tree:tree._label == "NP")
    # for subtree in subtrees:
    #     chunks.append(subtree)
    #     print(subtree)
    #
    #     subsubs = subtree.subtrees(filter = lambda tree:tree._label == "NP")
    #     count = 0
    #     for subsub in subsubs:
    #         count += 1
    #         print("   ",subsub)
    #     if count > 1:
    #         chunks.remove(subtree)
    #     # count = 1 as subtree == subsub, unless subsub has another NP branch which increases count
    #
    # return chunks

    chunks = []

    subtrees = tree.subtrees(filter = lambda tree:tree._label == "NP")
    for subtree_obj in subtrees:
        for subsubtree_obj in subtree_obj.subtrees(filter = lambda tree:tree._label == "NP"):
            if subtree_obj != subsubtree_obj:
                break
        else:
            chunks.append(subtree_obj)

    return chunks


if __name__ == "__main__":
    main()
