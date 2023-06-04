import node as nd
#* Version: 1.0

class DisjointSetForest:
    def __init__(self):
        self.nodes = {}
    
    def make_set(self, value):
        if value not in self.nodes:
            node = nd.Node(value)
            self.nodes[value] = node

    #* trova il rappresentante dell'insieme disgiunto
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



class DisjointSetLinkedList:
    def __init__(self):
        self.nodes = {}

    def make_set(self, value):
        node = nd.Node(value)
        self.nodes[value] = node

    #* trova il rappresentante dell'insieme disgiunto
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

        last_node2 = node2.last

        node2.last = node1.last
        last_node2.next = node1
        
        current_node = node1
        while current_node is not None:
            current_node.representative = node2
            current_node = current_node.next

        node2.size += node1.size
   
    #* unisce gli insiemi disgiunti con euristica dei pesi: concatena la lista più piccola alla più grande
    def euristic_union(self, value1, value2):
        node1 = self.find_set(value1)
        node2 = self.find_set(value2)

        if node1 is None or node2 is None or node1 == node2:
            return
        
        if node1.size < node2.size:
            self.union(value1, value2) 
        else:
            self.union(value2, value1)