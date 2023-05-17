class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self          # ogni nodo punta al proprio padre, 
                                    # la radice punta a se stessa ed è anche il rappresetnante dell'insieme disgiunto
        self.rank = 0

class DisjointSetForest:
    def __init__(self):
        self.nodes = {}
    
    def make_set(self, value):
        if value not in self.nodes:
            node = Node(value)
            self.nodes[value] = node

    # trova il rappresentante dell'insieme disgiunto
    def find_set(self, value):
        if value not in self.nodes:
            return None
        else:
            node = self.nodes[value]
            if node != node.parent:
                node.parent = self.find_set(node.parent.value)
            return node.parent
    
    def union(self, value1, value2):
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return
        
        self.link(node1, node2)

    def link(self, node1, node2):
        if node1.rank >= node2.rank:
            node2.parent = node1
        else:
            node1.parent = node2
            if node1.rank == node2.rank:
                node2.rank += 1