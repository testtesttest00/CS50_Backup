import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        return len(self.cells)

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)
        return len(self.cells)
        # empty sentences should not result as long as sentences are removed after marking the last mine


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            if not sentence.mark_mine(cell):
                self.knowledge.remove(sentence)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            if not sentence.mark_safe(cell):
                self.knowledge.remove(sentence)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Adds cell to set of moves made and marks cell as safe for class object and narrows every knowledge sentence
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # if cell == (0, 0):
        #     exit(1)

        # Gets a set of nearby cells
        nearby = set()
        for i in [cell[0] - 1, cell[0], cell[0] + 1]:
            for j in [cell[1] - 1, cell[1], cell[1] + 1]:
                if (i, j) == cell or (i, j) in self.safes:
                    continue
                elif (i, j) in self.mines:
                    count -= 1
                    continue
                if i in range(self.height) and j in range(self.width):
                    nearby.add((i, j))

        # Creates a new sentence of {nearby_cells}:{mine_count} while narrowing every existing knowledge sentences
        for sentence in self.knowledge:
                if nearby <= sentence.cells and nearby:
                    for cell_ in nearby:
                        sentence.cells.remove(cell_)
                    sentence.count -= count
        self.knowledge.append(Sentence(nearby, count))

        # When certain of safe/mine cells, marks cells respectively within class object and narrows every knowledge sentences
        def mark_knowledge(persistance = 0):
            # Persistance = 1 to allow for re-checks after knowledge sentences are narrowed
            updates = False
            persist = 1
            while persist:
                # print("Marking knowledge iteration")
                for sentence in self.knowledge:
                    # print(f"Checking for marking: {sentence.cells} = {sentence.count}")
                    if setcells := sentence.known_mines().copy():
                        for cells in setcells:
                            self.mark_mine(cells)
                        persist = persistance
                        updates = True
                    elif setcells := sentence.known_safes().copy():
                        for cells in setcells:
                            self.mark_safe(cells)
                        persist = persistance
                        updates = True
                persist -= 1
            return updates

        # Infers new sentences to be narrowed further, using newly narrowed sentences
        def infer_sentences(persistance = 0):
            # Persistance = 1 to allow for re-checks after knowledge sentences are narrowed
            updates = False
            persist = 1
            while persist:
                # print("Inferring sentences iteration")
                for sentence in self.knowledge:
                    if not sentence.cells:
                        self.knowledge.remove(sentence)
                        continue
                    # print(f"Checking for inference: {sentence.cells} = {sentence.count}")
                    for comparison in self.knowledge:
                        if sentence != comparison and sentence.cells <= comparison.cells:
                            for cell_ in sentence.cells:
                                comparison.cells.remove(cell_)
                            comparison.count -= sentence.count
                            persist = persistance
                            updates = True
                persist -= 1
            return updates

        while mark_knowledge(1) or infer_sentences(1):
            pass

        return

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        moves = []
        for move in self.safes:
            if move not in self.mines and move not in self.moves_made:
                moves.append(move)
        if moves:
            return random.choice(moves)
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        exit_flag = 0
        tried = [(None, None)]
        i = None
        j = None

        while (i, j) in self.moves_made or (i, j) in self.mines or (i, j) in tried:
            tried.append((i, j))
            i = random.randrange(self.height)
            j = random.randrange(self.width)
            exit_flag += 1
            if exit_flag > self.width * self.height:
                return None

        return (i, j)
