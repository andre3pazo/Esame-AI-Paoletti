import math


# La funzione line_intesection trova qual è il punto in cui si intersecano due rette.
def line_intersection(r1, r2):
    result = None
    if r1[0] != r2[0]:
        x = (r2[1]-r1[1])/(r1[0]-r2[0])
        y = r1[0]*x + r1[1]
        result = (x, y)
    return result


# La funzione verify_intersection verifica se due archi del grafo si incrociano.
def verify_intersection(intersect, node1, node2, node3, node4):
    if intersect is None:
        return False
    if (node1.x > intersect[0] > node2.x) or (node2.x > intersect[0] > node1.x):
        if (node3.x > intersect[0] > node4.x) or (node4.x > intersect[0] > node3.x):
            return True
    return False
