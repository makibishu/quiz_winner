import functools

ODDS = [0.3, 0.25, 0.2, 0.15, 0.1]
GOAL = 4

class Node:
    __slots__ = 'ID', 'probability', 'scores', 'children'

    count = 0
    probabilities = [0] * len(ODDS)

    def __init__(self, parent: 'Node', index: int) -> None:
        Node.count += 1
        self.ID = Node.count

        self.probability = parent.probability * ODDS[index]
        self.scores = parent.scores.copy()
        self.scores[index] += 1

        if max(self.scores) < GOAL:
            self.children = [Node(parent=self, index=i) for i in range(len(ODDS))]
        else:
            self.children = None
            Node.probabilities[index] += self.probability

            print(self)

            if index == (len(ODDS)-1):
                del parent
            del self
        
    def __repr__(self) -> str:
        return f'Node{self.ID}: {self.probability*100: .10f}%, {self.scores}'

class Root(Node):
    __slots__ = 'ID', 'probability', 'scores', 'children'

    def __init__(self):
        self.ID = 0
        self.probability = 1
        self.scores = [0] * len(ODDS)

        self.children = [Node(parent=self, index=i) for i in range(len(ODDS))]

tree = Root()

print('\n[Result]')
for i, p in enumerate(tree.probabilities):
    print(f'Player{i+1}: {p*100:.5f}%')