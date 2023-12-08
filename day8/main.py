import re


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.name} -> L:{self.left.name}  R:{self.right.name}'


class Graph:
    def __init__(self):
        self.starting_node = None
        self.nodes = {}

    def __str__(self):
        return str(list(self.nodes.values()))

    def add_node(self, name, left, right):
        node = self.nodes.get(name)

        if left != right:
            left_node = self.nodes.get(left, Node(left, None, None))
            right_node = self.nodes.get(right, Node(right, None, None))
        else:
            left_node = self.nodes.get(left, Node(left, None, None))
            right_node = left_node

        if not node:
            node = Node(name, left_node, right_node)
        else:
            node.left = left_node
            node.right = right_node

        self.nodes[name] = node
        self.nodes[left] = left_node
        self.nodes[right] = right_node

        if name == 'AAA':
            self.starting_node = node

    def walk(self, pattern):
        steps = 0
        current_node = self.starting_node

        while current_node.name != 'ZZZ':
            steps += 1

            direction = next(pattern)
            if direction == 'L':
                current_node = current_node.left
            else:
                current_node = current_node.right

        return steps


class Pattern:
    def __init__(self, steps):
        self.steps = steps
        self.index = 0
        self.lenght = len(self.steps)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.lenght:
            self.index += 1
            return self.steps[self.index - 1]
        else:
            self.index = 1
            return self.steps[self.index - 1]

    def __str__(self):
        return self.steps


with open('day8/input.txt', 'r') as f:
    lines = f.readlines()

pattern = Pattern(lines[0].strip())
nodes_def = lines[2:]

graph = Graph()
for single_def in nodes_def:
    nodes = re.findall(r'[A-Z]+', single_def)
    graph.add_node(nodes[0], nodes[1], nodes[2])

# print(graph)
print(f'Steps:\n{graph.walk(pattern)}')
