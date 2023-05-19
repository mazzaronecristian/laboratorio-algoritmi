class Node:
    def __init__(self, value):
        self.value = value
        self.representative = self  # ogni nodo punta al rappresentate del proprio insieme disgiunto (inizialmente se stesso)
        self.next = None
        self.last = self     # puntatore alla coda della lista
        self.size = 1

class DisjointSetLinkedList:
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
        return node.representative

    #* unisce gli insiemi disgiunti senza euristica, concateno node1 a node2
    def union(self, value1, value2):            
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return

        last_node2 = node2
        while last_node2.next is not None:
            last_node2 = last_node2.next

        last_node2.next = node1
        
        current_node = node1
        while current_node is not None:
            current_node.representative = node2
            current_node = current_node.next

        node2.size += node1.size
   
    def euristic_union(self, value1, value2):
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return
        
        if node1.size < node2.size:
            self.union(value1, value2) 
        else:
            self.union(value2, value1)