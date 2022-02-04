import math


# L'euristica MRV viene usata per selezionare il prossimo nodo da cui eseguire l'algoritmo backtrack.
def mrv(unassigned_variables):
    min = math.inf
    next_value = None
    for v in unassigned_variables:
        if len(v.domain) < min:
            min = len(v.domain)
            next_value = v
    return next_value


# La funzione undo_inference viene usata per "tornare indietro" in caso di fallimento dell'inferenza.
def undo_inference(color, inferences):
    for y in inferences:
        if color not in y.domain:
            y.domain.append(color)


# La funzione forward_checking è una delle procedure di inferenza usata nell'esecuzione dell'algoritmo backtracking.
# La procedura fornisce in output la lista dei nodi il cui dominio è stato modificato e un valore booleano
# pari a False se l'inferenza fallisce, ovvero se uno dei nodi vede il suo dominio annullarsi, evidenziando
# quindi un'inconsistenza.
def forward_checking(unassigned_variables, v, color):
    inferences = []
    result = True
    for y in v.neighbours:
        if y in unassigned_variables:
            if color in y.domain:
                y.domain.remove(color)
                inferences.append(y)
            if len(y.domain) == 0:
                result = False
                break
    return inferences, result


# L'algoritmo presentato qui è l'implementazione che usa come procedura di inferenza il forward checking.
def backtrack_fwchecking(assigned_variables, unassigned_variables):
    if len(unassigned_variables) == 0:
        return assigned_variables
    v = mrv(unassigned_variables)
    for color in v.domain:
        inferences = [[], False]
        consistent = True
        for neigh in v.neighbours:
            if neigh.color == color:
                consistent = False
        # Se assegnare il colore "color" al nodo v è consistente con gli altri assegnamenti già effettuati allora
        # possiamo procedere con l'assegnamento e con l'inferenza.
        if consistent:
            v.color = color
            unassigned_variables.remove(v)
            assigned_variables.append(v)
            inferences = forward_checking(unassigned_variables, v, color)
            if inferences[1]:
                result = backtrack_fwchecking(assigned_variables, unassigned_variables)
                if result is not None:
                    return result
        v.color = None
        if v in assigned_variables:
            assigned_variables.remove(v)
            unassigned_variables.append(v)
        undo_inference(color, inferences[0])
    return None


# remove_inconsistent_value viene usato nell'algoritmo di inferenza ac_3. La sua funzione è rimuovere dal dominio
# delle variabili quei valori che siano inconsistenti con altri domini dei nodi vicini.
def remove_inconsistent_value(arc):
    removed_values = []
    okay = False
    for x in arc[0].domain:
        for y in arc[1].domain:
            if y != x:
                okay = True
                break
        if not okay:
            arc[0].domain.remove(x)
            removed_values.append(x)
    return removed_values


# L'algoritmo ac_3 serve per verificare la consistenza d'arco. Viene fornita in output la lista di variabili i cui
# domini sono stati modificati e quali colori vi sono stati sottratti, oltre a un booleano che assume False se la
# consistenza d'arco non può essere mantenuta.
def ac_3(node, unassigned_vars):
    queue = []
    inferences = []
    for y in node.neighbours:
        if y in unassigned_vars:
            queue.append([node, y])
    while len(queue) > 0:
        arc = queue[0]
        queue.remove(arc)
        r = remove_inconsistent_value(arc)
        if len(r) > 0:
            inferences.append((arc[0], r))
            if len(arc[0].domain) == 0:
                return False, inferences
            for k in node.neighbours:
                if k in unassigned_vars:
                    if k != arc[1]:
                        queue.append([k, node])
    return True, inferences


# Questa seconda variante del backtracking fa uso dell'algoritmo ac_3 per effettuare l'inferenza.
def backtrack_mac(assigned_variables, unassigned_variables):
    if len(unassigned_variables) == 0:
        return assigned_variables
    v = mrv(unassigned_variables)
    for color in v.domain:
        inferences = []
        consistent = True
        ac_inf = []
        for neigh in v.neighbours:
            if neigh.color == color:
                consistent = False
        if consistent:
            v.color = color
            unassigned_variables.remove(v)
            assigned_variables.append(v)
            arc_consistent = True
            for y in v.neighbours:
                if y in unassigned_variables:
                    if color in y.domain:
                        y.domain.remove(color)
                        inferences.append(y)
                        ac = ac_3(y, unassigned_variables)
                        arc_consistent = ac[0]
                        ac_inf.append(ac[1])
                        if not arc_consistent:
                            break
            if arc_consistent:
                result = backtrack_mac(assigned_variables, unassigned_variables)
                if result is not None:
                    return result
        v.color = None
        if v in assigned_variables:
            assigned_variables.remove(v)
            unassigned_variables.append(v)
        undo_inference(color, inferences)
        for inf in ac_inf:
            for i in inf:
                for col in i[1]:
                    if col not in i[0].domain:
                        i[0].domain.append(col)
    return None
