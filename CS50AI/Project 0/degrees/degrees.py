import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]} # {row[id]} is a set ({...} - set vs {... : ...} - dict)
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass

# example resultant dictionaries (people, names, movies)
# people = {"0001":{"name":"abc", "birth":"1999", "movies":{"1101","1139"}}, "0004":{"name":"def", "birth":"1982", "movies":{"1101"}}}
# names = {"abc":{"0001"}, "def":{"0004"}}
# movies = {"1101":{"title":"a", "year":"2010", "stars":{"0001","0004"}}, "1139":{"title":"b", "year":"2011", "stars":{"0001"}}}


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path # pre-add path = [(sourceplusname1MOVIE, name1), (name1plusname2MOVIE, name2), ...]
        for i in range(degrees):
            person1 = people[path[i][1]]["name"] # person1.id = path[i][1], person2.id = path[i + 1][1]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"] # movie.id = path[i + 1][0]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target): # both are person_id
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # idea:
    # initial state: tuple[1] == source // goal state: tuple[1] == target
    # actions(state) = neighbors_for_person(person_id)[ for _ in range(len(neighbors_for_person(person_id))) ]
    if source == target:
        return []

    def create_path(node):
        path = []
        while node.parent:
            path.append(node.state)
            node = node.parent
        # path = [(sourceplusname1MOVIE, name1), (name1plusname2MOVIE, name2), ...]
        path.reverse()
        return path

    frontier = QueueFrontier()
    frontier.add(Node((None, source), None, None))
    explored = StackFrontier()
    while frontier.frontier:
        magnified = frontier.remove()
        neighbors = neighbors_for_person(magnified.state[1])
        for tuple in neighbors:
            new = Node(tuple, magnified, tuple)
            if new.state[1] == target:
                return create_path(new)
            if not explored.contains_state(tuple) and not frontier.contains_state(tuple):
                frontier.add(new)
        explored.add(magnified)

    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    # names: dict() of "name":set("id", ...) => persons_ids = list(set("id", ...))
    person_ids = list(names.get(name.lower(), set())) # dict.get(key, default=None) returns value of "key:set(names)" otherwise default
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0] # person_ids = {"id"} //set of len = 1, index into with [0] to return value rather than set


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors
# neighbors: set() of tuple[2]

if __name__ == "__main__":
    main()
