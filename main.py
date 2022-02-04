import random as ran
import node
import backtrack
from timeit import default_timer as timer
from matplotlib import pyplot as plt


if __name__ == '__main__':
    nodes = []
    lines = []
    ass_nodes = []
    n = int(input("Insert number of nodes: "))
    b = int(input("Press 1 for forward checking or 2 for MAC: "))
    for i in range(n):
        new_node = node.Node(ran.random(), ran.random(), i + 1, d=["red", "green", "blue", "yellow"])
        nodes.append(new_node)
    node.build_graph(nodes, lines)
    if b == 1:
        backtrack.backtrack_fwchecking(ass_nodes, nodes)
    elif b == 2:
        backtrack.backtrack_mac(ass_nodes, nodes)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    for n in ass_nodes:
        print()
        node.print_node(n)
        plt.plot(n.x, n.y, marker="o", color=n.color)
        print("Its neighbours are: ")
        for neigh in n.neighbours:
            node.print_node(neigh)
            plt.plot([n.x, neigh.x], [n.y, neigh.y], color="grey")
    plt.show()
    for number in range(80):
        somma_fw = 0
        somma_MAC = 0
        for j in range(100):
            nodes = []
            lines = []
            ass_nodes = []
            for i in range(number):
                new_node = node.Node(ran.random(), ran.random(), i + 1, d=["red", "green", "blue", "yellow"])
                nodes.append(new_node)
            node.build_graph(nodes, lines)
            start_fw = timer()
            r = backtrack.backtrack_fwchecking(ass_nodes, nodes)
            end_fw = timer()
            somma_fw += end_fw-start_fw
            nodes = []
            lines = []
            ass_nodes = []
            for i in range(number):
                new_node = node.Node(ran.random(), ran.random(), i + 1, d=["red", "green", "blue", "yellow"])
                nodes.append(new_node)
            node.build_graph(nodes, lines)
            start_MAC = timer()
            s = backtrack.backtrack_mac(ass_nodes, nodes)
            end_MAC = timer()
            somma_MAC += end_MAC - start_MAC
        print()
        print(f'Tempo medio per {number} nodi per fw: {round(somma_fw / 100, 5)}')
        print(f'Tempo medio per {number} nodi per MAC: {round(somma_MAC / 100, 5)}')
        print()
        print('Con tre valori del dominio invece:')
        plt.plot(number, somma_fw / 100, marker="o", color="red")
        plt.plot(number, somma_MAC / 100, marker="o", color="blue")
        somma_fw = 0
        somma_MAC = 0
        for j in range(100):
            nodes = []
            lines = []
            ass_nodes = []
            for i in range(number):
                new_node = node.Node(ran.random(), ran.random(), i + 1, d=["red", "green", "blue"])
                nodes.append(new_node)
            node.build_graph(nodes, lines)
            start_fw = timer()
            r = backtrack.backtrack_fwchecking(ass_nodes, nodes)
            end_fw = timer()
            somma_fw += end_fw - start_fw
            nodes = []
            lines = []
            ass_nodes = []
            for i in range(number):
                new_node = node.Node(ran.random(), ran.random(), i + 1, d=["red", "green", "blue"])
                nodes.append(new_node)
            node.build_graph(nodes, lines)
            start_MAC = timer()
            s = backtrack.backtrack_mac(ass_nodes, nodes)
            end_MAC = timer()
            somma_MAC += end_MAC - start_MAC
        print(f'Tempo medio per {number} nodi per fw: {round(somma_fw / 100, 5)}')
        print(f'Tempo medio per {number} nodi per MAC: {round(somma_MAC / 100, 5)}')
        print()
