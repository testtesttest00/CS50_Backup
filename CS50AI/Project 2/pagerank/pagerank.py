import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            # (?:[^>]*?) - Non-capturing group that matches any character except > (0 or more times, non-greedy).
            # ([^\"]*) - Capturing group that matches any character except " (0 or more times).

            # Removes inclusion of self-linking pages
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus (e.g. remove link "A.html -> Z.html" if corpus only includes A.html - E.html)
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages
    # pages = {"a.html":{"b.html", "c.html"}, "b.html":{"a.html", "d.html", "e.html"}, ...}


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    n_destinations = len(corpus[page])
    try:
        link_probability = 1 / n_destinations
    except ZeroDivisionError:
        link_probability = 0
    n_nondestinations = len(corpus) - n_destinations
    shared_probability = 1 / n_nondestinations

    distribution = dict()
    for destination in corpus:
        distribution[destination] = (1 - damping_factor) * shared_probability
        if destination in corpus[page]:
            distribution[destination] = damping_factor * link_probability

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sample = dict()
    for page in corpus:
        sample[page] = 0

    current = random.choice(list(corpus))
    sample[current] += 1
    for _ in range(n-1):
        next = transition_model(corpus, current, damping_factor)
        current = random.choices(list(next), weights=dict.values(next), k=1)[0]
        sample[current] += 1

    for page in sample:
        sample[page] = sample[page] / n

    return sample


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Create and initialise return dictionary, rank
    rank = dict()
    shared_probability = 1 / len(corpus)
    for page in corpus:
        rank[page] = shared_probability

    # If page links to nothing, treat it as though it links to every page in the corpus
    for page in corpus:
        if not corpus[page]:
            corpus[page] = set(corpus)

    # Creates a dictionary to get pages that link to current page
    previous = dict()
    for page in corpus:
        for prev_page in corpus:
            if page in corpus[prev_page]:
                if page not in previous:
                    previous[page] = set()
                previous[page].add(prev_page)

    # Recursively calculates page_rank until difference >= 0.001 is False, ending while loop
    difference = True
    while difference:
        difference = False
        for page in corpus:
            initial_save = rank[page]
            previous_value = 0
            for link in previous[page]:
                previous_value += rank[link] / len(corpus[link])
            rank[page] = (1 - damping_factor) / len(corpus) + damping_factor * previous_value
            if rank[page] - initial_save <= -0.001 or rank[page] - initial_save >= 0.001:
                difference += True

    return rank


if __name__ == "__main__":
    main()
