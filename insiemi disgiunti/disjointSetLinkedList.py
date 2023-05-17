class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self  # ogni nodo punta al rappresentate del proprio insieme disgiunto (inizialmente se stesso)
        self.next = None
        self.size = 1

class DisjointSetLL:
    def __init__(self):
        self.nodes = {}

    def make_set(self, value):
        node = Node(value)
        self.nodes[value] = node

    # trova il rappresentante dell'insieme disgiunto
    def find_set(self, value):
        if value not in self.nodes:
            return None
        
        node = self.nodes[value]
        return node.parent

    # unisce gli insiemi disgiunti senza euristica    
    def union(self, value1, value2):
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return
        
        node2.parent = node1
        node1.size += node2.size
        node1.next = node2

        while node2.next is not None:
            node2 = node2.next
            node2.parent = node1
        
    # unisce gli insiemi disgiunti con euristica della size: la lista con size minore viene attaccata alla lista con size maggiore
    def euristic_union(self, value1, value2):
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return
        
        if node1.size < node2.size:
            self.union(value2, value1) 
        else:
            self.union(value1, value2)