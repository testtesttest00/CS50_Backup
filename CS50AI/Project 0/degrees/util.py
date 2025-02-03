class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier(): # Depth-First Search
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state): # creates array of bool values, use any to check for at least 1 True
        return any(node.state == state for node in self.frontier) # any([...]) returns True if >= 1 more elements in [...] == True

    def empty(self): # checks if frontier is empty
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] # takes last-appended node
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier): # Inherit search approach, redefine .remove() for Breadth-First Search

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0] # takes oldest added node
            self.frontier = self.frontier[1:]
            return node
