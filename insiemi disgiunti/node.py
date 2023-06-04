#* classe Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.set = None

#* crea una funzione random_nodes che, dato in ingresso un intero n, ritorna un array di n nodi con valori compresi tra 0 e n-1
def random_nodes(n):
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
    return nodes    
