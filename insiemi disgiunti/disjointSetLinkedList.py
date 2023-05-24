class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.set = None

# class DisjointSetLinkedList:
#     def __init__(self):
#         self.nodes = {}

#     def make_set(self, value):
#         node = Node(value)
#         self.nodes[value] = node

#     #* trova il rappresentante dell'insieme disgiunto
#     def find_set(self, value):
#         if value not in self.nodes:
#             return None
        
#         node = self.nodes[value]
#         return node.representative

#     #* unisce gli insiemi disgiunti senza euristica, concateno node1 a node2
#     def union(self, value1, value2):            
#         node1 = self.find_set(value1)
#         node2 = self.find_set(value2)

#         if node1 is None or node2 is None or node1 == node2:
#             return

#         last_node2 = node2.last

#         node2.last = node1.last
#         last_node2.next = node1
        
#         current_node = node1
#         while current_node is not None:
#             current_node.representative = node2
#             current_node = current_node.next

#         node2.size += node1.size
   
#     #* unisce gli insiemi disgiunti con euristica dei pesi: concatena la lista più piccola alla più grande
#     def euristic_union(self, value1, value2):
#         node1 = self.find_set(value1)
#         node2 = self.find_set(value2)

#         if node1 is None or node2 is None or node1 == node2:
#             return
        
#         if node1.size < node2.size:
#             self.union(value1, value2) 
#         else:
#             self.union(value2, value1)

class Set:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.size = 1
    
class DisjointSetLinkedList:
    def __init__(self):
        self.sets = []
        self.elements = {}
    
    def make_set(self, value):
        if value in self.elements:
            return
        node = Node(value)
        set = Set(node)
        node.set = set
        self.sets.append(set)
        self.elements[value] = node
    
    def find_set(self, value):
        if value in self.elements:
            return self.elements[value].set.head
        else:
            return None
    
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

    def euristic_union(self, value1, value2):
        rep1 = self.find_set(value1)
        rep2 = self.find_set(value2)

        if rep1 is None or rep2 is None or rep1 == rep2:
            return
        
        if rep1.set.size < rep2.set.size:
            self.union(value1, value2)
        else:
            self.union(value2, value1)
        

    