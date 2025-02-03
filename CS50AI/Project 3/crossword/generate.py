import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
        # (dict) assignment.items() >> {key:value}.items() >> (list) [(tuple) (key, value)]
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains:
                for word in self.domains[variable].copy():
                    if len(word) != variable.length:
                        self.domains[variable].remove(word)

        return

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        if shared := self.crossword.overlaps[x, y]:
            edit = False
            for xword in self.domains[x].copy():
                viable = False
                for yword in self.domains[y]:
                    if xword[shared[0]] == yword[shared[1]]:
                        viable = True
                if not viable:
                    self.domains[x].remove(xword)
                    edit = True

            return edit

        return True

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = arcs
        if queue == None:  # if arcs == [], queue will remain empty
            queue = []
            for x in self.domains:
                for y in self.crossword.neighbors(x):
                    queue.append((x, y))

        while queue:
            pair = queue.pop(0)
            if self.revise(pair[0], pair[1]):
                if not self.domains[pair[0]]:
                    return False
                for neighbor in self.crossword.neighbors(pair[0]):
                    queue.append((neighbor, pair[0]))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for variable in self.domains:
            if variable not in assignment:
                return False

        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        for variable in assignment:
            if not variable:
                continue

            if len(assignment[variable]) != variable.length:
                return False

            neighbors = self.crossword.neighbors(variable)
            for neighbor in neighbors:
                if neighbor not in assignment:
                    continue

                if assignment[variable] == assignment[neighbor]:
                    return False

                indices = self.crossword.overlaps[variable, neighbor]
                if assignment[variable][indices[0]] != assignment[neighbor][indices[1]]:
                    return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        order = {
            word : 0
            for word in self.domains[var]
        }
        # alternative
        # order = dict()
        # for word in self.domains[var]:
        #     order[word] = 0
        neighbors = self.crossword.neighbors(var)
        for word in order:
            for neighbor in neighbors:
                indices = self.crossword.overlaps[var, neighbor]
                for compare in self.domains[neighbor]:
                    if word[indices[0]] != compare[indices[1]] or word == compare:
                        order[word] += 1
            if word in assignment.values():
                order[word] = float("inf")

        order = list(pair[0] for pair in sorted(order.items(), key=lambda word: word[1]))
        return order

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Dictionary of {Variable : Remaining values}
        unassigned = {var : len(self.domains[var]) for var in self.domains if var not in assignment}

# Error: Degree sort overrides Remaining values sort
#        # Dictionary of {Variable : Number of neighbors}
#        unassigned = {
#            pair[0] : len(self.crossword.neighbors(pair[0]))
#            for pair in sorted(unassigned.items(), key=lambda pair : pair[1])
#            }
#        # List of [Variables] sorted by number of neighbors
#        unassigned = [var[0] for var in sorted(unassigned.items(), key=lambda pair : pair[1], reverse = True)]

        # Dictionary of {Variables tying for minimum remaining values : Number of neighbors}
        unassigned = {
            var : len(self.crossword.neighbors(var))
            for var in unassigned
            if unassigned[var] == min(unassigned.values())
            }
        # List of [Variables with minimum remaining values] sorted by number of neighbors
        unassigned = [var[0] for var in sorted(unassigned.items(), key=lambda pair : pair[1], reverse = True)]

        return unassigned[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            if self.consistent(assignment):
                return assignment
            return None
        var = self.select_unassigned_variable(assignment)
        dom = self.order_domain_values(var, assignment)
        while dom.copy():
            val = dom.pop(0)
            assignment[var] = val

            # Inference algorithm
            # ori_var = var
            # inferences = []
            # tested = 0
            # while len(inferences) == 0 or tested != len(inferences):
            #     for neighbor in self.crossword.neighbors(var):
            #
# Error occurs as self.domains [v/n copy] overwrites original (share same key on dict)
#                 vcopy = Variable(var.i, var.j, var.direction, var.length)
#                 ncopy = Variable(neighbor.i, neighbor.j, neighbor.direction, neighbor.length)
            #
            #         vcopy = Variable(-var.i, -var.j, var.direction, var.length)
            #         ncopy = Variable(-neighbor.i, -neighbor.j, neighbor.direction, neighbor.length)
            #         self.domains[vcopy] = set([val])
            #         self.domains[ncopy] = self.domains[neighbor].copy()
            #         self.crossword.overlaps[vcopy, ncopy] = self.crossword.overlaps[var, neighbor]
            #         self.crossword.overlaps[ncopy, vcopy] = self.crossword.overlaps[neighbor, var]
            #         self.ac3(arcs = [(ncopy, vcopy)])
            #         if len(self.domains[ncopy]) == 1 and (neighbor, list(self.domains[ncopy])[0]) not in inferences:
            #             inferences.append((neighbor, list(self.domains[ncopy])[0]))
            #         del self.domains[vcopy]
            #         del self.domains[ncopy]
            #         del self.crossword.overlaps[vcopy, ncopy]
            #         del self.crossword.overlaps[ncopy, vcopy]
            #     if not inferences:
            #         break
            #     var = inferences[tested][0]
            #     val = inferences[tested][1]
            #     tested += 1
            # for neighbor, val in inferences:
            #     assignment[neighbor] = val

            # Alternate inference algorithm
            ori_var = var
            inferences = []
            tested = 0
            while len(inferences) == 0 or tested != len(inferences):
                for neighbor in self.crossword.neighbors(var):
                    var_dom = self.domains[var].copy()
                    self.domains[var] = set([val])
                    neighbor_dom = self.domains[neighbor].copy()
                    self.ac3(arcs = [(neighbor, var)])
                    if len(self.domains[neighbor]) == 1 and (neighbor, list(self.domains[neighbor])[0]) not in inferences:
                        inferences.append((neighbor, list(self.domains[neighbor])[0]))
                    self.domains[var] = var_dom
                    self.domains[neighbor] = neighbor_dom
                if not inferences:
                    break
                var = inferences[tested][0]
                val = inferences[tested][1]
                tested += 1
            for neighbor_var, neighbor_val in inferences:
                assignment[neighbor_var] = neighbor_val

            if full := self.backtrack(assignment):
                return full

            # If not using inference algorithm
            # del assignment[var]

            # If using any inference algorithm
            del assignment[ori_var]
            for neighbor_var, _ in inferences:
                del assignment[neighbor_var]

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
