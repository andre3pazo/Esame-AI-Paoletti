import math
import line
import random as ran


class Node:

    def __init__(self, x, y, n="Node", c=None, d=None):
        if d is None:
            d = []
        self.name = n
        self.x = x
        self.y = y
        self.neighbours = []
        self.not_neighbours = []
        self.connected = False
        self.color = c
        self.domain = d

    def distance(self, n2):
        return math.sqrt(math.pow((self.x - n2.x), 2) + math.pow((self.y - n2.y), 2))

    # La funzione line_through_nodes calcola il coefficiente angolare e il termine noto dell'equazione della retta
    # passante per due nodi sotto forma di tupla (contenente coefficiente angolare e termine noto dell'equazione
    # della retta).
    def line_through_nodes(self, n2):
        m = (self.y - n2.y) / (self.x - n2.x)
        q = self.y - m * self.x
        return [m, q]


def print_node(node):
    print(f'Node name: {node.name}')
    print(f'Position: ({node.x}, {node.y})')


def select_closest(x):
    closest = None
    min = math.inf
    for y in x.not_neighbours:
        dist = x.distance(y)
        if dist < min:
            min = dist
            closest = y
    return closest


def connect_neighbour(x, lines):
    loop = True
    while loop:
        y = select_closest(x)
        okay = True
        if y is not None:
            r = x.line_through_nodes(y)
            for s in lines:
                i = line.line_intersection(r, s[0])
                if line.verify_intersection(i, x, y, s[1], s[2]):
                    x.not_neighbours.remove(y)
                    y.not_neighbours.remove(x)
                    okay = False
                    break
            if okay:
                x.not_neighbours.remove(y)
                y.not_neighbours.remove(x)
                x.neighbours.append(y)
                y.neighbours.append(x)
                lines.append((r, x, y))
                loop = False
        else:
            loop = False
        if len(x.not_neighbours) == 0:
            x.connected = True


def build_graph(nodes, lines):
    new_graph = []
    for n in nodes:
        new_graph.append(n)
    for i in range(len(nodes)):
        not_neigh = []
        for j in range(len(nodes)):
            if i != j:
                not_neigh.append(nodes[j])
        nodes[i].not_neighbours = not_neigh
    while len(new_graph) > 0:
        i = int(ran.random() * len(new_graph))
        x = new_graph[i]
        connect_neighbour(x, lines)
        if x.connected:
            new_graph.remove(x)
