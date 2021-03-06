# Esame-AI-Paoletti
Progetto relativo all'esame di Intelligenza Artificiale dell'anno accademico 2021/22.

Autore: Andrea Paoletti

Il progetto consiste nell'implementazione dell'algoritmo di backtracking con forward checking e con MAC.
L'elaborato consiste di quattro moduli sorgente: 
1) "main.py", che non contiene nessuna classe o funzione fondamentale per il funzionamento del programma, ma contiene solamente il main, nel quale vengono generate istanze di problemi di colorazione di grafi casuali e vengono eseguiti alcuni test sugli algoritmi da studiare. In particolare gli algoritmi vengono eseguiti e ne vengono misurati e infine confrontati i tempi, anche attraverso la creazione di grafici esplicativi attraverso la libreria matplotlib;
2) "backtrack.py" contiene tutte le funzioni necessarie per il corretto funzionamento dell'algoritmo di backtracking. Contiene quindi l'algoritmo di backtracking, la funzione di forward checking, la funzione di MAC e le altre funzioni ausiliare di cui si avvalgono questi algoritmi;
3) "node.py" è il modulo contenente la classe Node, la quale contiene tutti gli attributi e i metodi indispensabili per caratterizzare i vertici del grafo al fine di otervi eseguire correttamente gli algoritmi di backtracking. Contiene inoltre la funzione build_graph, usata proprio per generare istanze di grafi a partire da un insieme di vertici. build_graph si avvale dell'aiuto di due funzioni ausiliarie, connect_neighbour e select_closest, il cui scopo è quello di individuare durante il processo di costruzione del grafo quale sia il prossimo nodo da collegare e quindi collegarlo, se possibile;
4) "line.py" ha invece il compito di gestire le rette (corrispondenti agli archi del grafo) al fine di verificare quali archi possono essere tracciati e quali no - secondo la formulazione del problema infatti non è possibile tracciare un nuovo arco qualora questo intersecasse un arco già esistente.
