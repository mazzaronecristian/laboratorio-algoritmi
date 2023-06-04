import node as nd

#* implementazione degli insiemi disgiunti con liste concatenate
class Set:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.size = 1
    
class DisjointSetLinkedList:
    def __init__(self):
        self.sets = []
        self.elements = {}
    
    #* crea un nuovo insieme disgiunto con un solo elemento
    def make_set(self, value):
        if value in self.elements:
            return
        node = nd.Node(value)
        set = Set(node)
        node.set = set
        self.sets.append(set)
        self.elements[value] = node
    
    #* trova il rappresentante dell'insieme disgiunto
    def find_set(self, value):
        if value in self.elements:
            return self.elements[value].set.head
        else:
            return None
    
    #* unisce gli insiemi disgiunti senza euristica, concateno set1 a set2
    def union(self, value1, value2):
        rep1 = self.find_set(value1)
        rep2 = self.find_set(value2)

        if rep1 is None or rep2 is None or rep1 == rep2:
            return

        set1 = rep1.set
        set2 = rep2.set
        
        last_node2 = set2.tail
        set2.tail = set1.tail
        last_node2.next = set1.head

        current_node = set1.head
        while current_node is not None:
            current_node.set = set2
            current_node = current_node.next
            set2.size += 1
        
        self.sets.remove(set1)

    #* unisce gli insiemi disgiunti con euristica dei pesi
    def euristic_union(self, value1, value2):
        rep1 = self.find_set(value1)
        rep2 = self.find_set(value2)

        if rep1 is None or rep2 is None or rep1 == rep2:
            return
        
        if rep1.set.size < rep2.set.size:
            self.union(value1, value2)
        else:
            self.union(value2, value1)
        


#* implementazione degli insiemi disgiunti con foreste
class Forest:
    def __init__(self, node):
        self.head = node
        self.rank = 0

class DisjointSetForest:
    def __init__(self):
        self.forests = []
        self.elements = {}
    
    #* crea un nuovo insieme disgiunto con un solo elemento
    def make_set(self, value):
        if value in self.elements:
            return
        node = nd.Node(value)
        forest = Forest(node)
        node.set = forest
        self.forests.append(forest)
        self.elements[value] = node
    
    #* trova il rappresentante dell'insieme disgiunto
    def find_set(self, value):
        if value not in self.elements:
            return None
        else:
            node = self.elements[value]
            if node != node.set.head:
                node.set.head = self.find_set(node.set.head.value)
            return node.set.head
   
    #* unisce gli insiemi disgiunti tenendo in considerazione il rank delle foreste
    def link(self, node1, node2):
        if node1 is None or node2 is None or node1 == node2:
            return
        if node1.set.rank > node2.set.rank:
            node2.set.head = node1
            self.forests.remove(node2.set)
        else:
            node1.set.head = node2
            self.forests.remove(node1.set)
            if node1.set.rank == node2.set.rank:
                node2.set.rank += 1

    def union(self, value1, value2):
        self.link( self.find_set(value1), self.find_set(value2) )

    def euristic_union(self, value1, value2):
        self.union(value1, value2)