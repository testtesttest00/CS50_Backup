import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and # Check for known trait value (can be left out as None != True if person in subset)
             people[person]["trait"] != (person in have_trait)) # Check if trait value is both True and in subset
            for person in names # Go through each person to make sure all known trait values that are True are in subset, have_trait
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                # Finds the probability of every possible subset of a family having one/two gene(s) given the subset with known traits

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Math logic from CS50 Duck:
    # 1.    P(A, B, C, D, ...) = P(A) * P(B) * P(C) * P(D), ..., where P(X) is the probability of an individual event (i.e. gene count or trait)
    # 2.    Normalising constant, c = sum(P(A, B, C, D), ...), where P(X, Y, Z, ...) is a joint probability, for all joint probabilities
    # 3.    Normalised probability, P(A) = sum(P(A, B, C, D), P(A, E, F, G), ...) / c
    # Normalising needed as (Σ all joint probabilities) != 1, some subsets are excluded as their trait values violate observation

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    p_people = list()

    for person in people:
        p_current = 1
        n = 0
        if person in one_gene:
            n = 1
        elif person in two_genes:
            n = 2

        # P(traits)
        if person in have_trait:
            p_current *= PROBS["trait"][n][True]
        else:
            p_current *= PROBS["trait"][n][False]

        # P(traits) * P(genes)
        if not people[person]["mother"] or not people[person]["father"]:
            p_current *= PROBS["gene"][n]
        else:
            # Probability that gene came from respective parent
            p_parent = {people[person]["mother"] : 0, people[person]["father"] : 0}

            # P(gene passed down) = P(gene) * P(non-mutation) + P(non-gene) * P(mutation)
            for parent in p_parent:
                if parent in one_gene:
                    p_parent[parent] = 0.5  # 0.5 * (1 - PROBS["mutation"]) + 0.5 * (PROBS["mutation"])
                elif parent in two_genes:
                    p_parent[parent] = 1 - PROBS["mutation"]  # 1 * (1 - PROBS["mutation"]) + 0 * (PROBS["mutation"])
                else:
                    p_parent[parent] = PROBS["mutation"] # 0 * (1 - PROBS["mutation"]) + 1 * (PROBS["mutation"])

            if n == 0:
                p_current *= (1 - p_parent[people[person]["mother"]]) * (1 - p_parent[people[person]["father"]])
            elif n == 1:
                p_current *= (p_parent[people[person]["mother"]]) * (1 - p_parent[people[person]["father"]]) + \
                            (1 - p_parent[people[person]["mother"]]) * (p_parent[people[person]["father"]])
            else:
                p_current *= (p_parent[people[person]["mother"]]) * (p_parent[people[person]["father"]])

        p_people.append(p_current)

    joint = 1
    for p_person in p_people:
        joint *= p_person
    return joint


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p
    return


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # total = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        # difference = 1 - total
        # probabilities[person]["gene"][0] += probabilities[person]["gene"][0] / total * difference
        # probabilities[person]["gene"][1] += probabilities[person]["gene"][1] / total * difference
        # probabilities[person]["gene"][2] += probabilities[person]["gene"][2] / total * difference

        # total = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        # difference = 1 - total
        # probabilities[person]["trait"][True] += probabilities[person]["trait"][True] / total * difference
        # probabilities[person]["trait"][False] += probabilities[person]["trait"][False] / total * difference

        # p += p / total * difference
        # p += p * (1 - total)  / total
        # p += p * (1 / total -1)
        # p += p / total - p
        # p = p / total

        total = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        probabilities[person]["gene"][0] = probabilities[person]["gene"][0] / total
        probabilities[person]["gene"][1] = probabilities[person]["gene"][1] / total
        probabilities[person]["gene"][2] = probabilities[person]["gene"][2] / total

        total = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        probabilities[person]["trait"][True] = probabilities[person]["trait"][True] / total
        probabilities[person]["trait"][False] = probabilities[person]["trait"][False] / total
    return


if __name__ == "__main__":
    main()
