class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.set = None

class Forest:
    def __init__(self, node):
        self.head = node
        self.rank = 0


class DisjointSetForest:
    def __init__(self):
        self.forests = []
        self.elements = {}
    
    def make_set(self, value):
        if value in self.elements:
            return
        node = Node(value)
        forest = Forest(node)
        node.set = forest
        self.forests.append(forest)
        self.elements[value] = node
    
    def find_set(self, value):
        if value not in self.elements:
            return None
        else:
            node = self.elements[value]
            if node != node.set.head:
                node.set.head = self.find_set(node.set.head.value)
            return node.set.head
   
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



# class DisjointSetForest:
#     def __init__(self):
#         self.nodes = {}
    
#     def make_set(self, value):
#         if value not in self.nodes:
#             node = Node(value)
#             self.nodes[value] = node

#     # trova il rappresentante dell'insieme disgiunto
#     def find_set(self, value):
#         if value not in self.nodes:
#             return None
#         else:
#             node = self.nodes[value]
#             if node != node.parent:
#                 node.parent = self.find_set(node.parent.value)
#             return node.parent
    
#     def union(self, value1, value2):
#         node1 = self.find_set(value1)
#         node2 = self.find_set(value2)

#         if node1 is None or node2 is None or node1 == node2:
#             return
        
#         self.link(node1, node2)

#     def link(self, node1, node2):
#         if node1.rank >= node2.rank:
#             node2.parent = node1
#         else:
#             node1.parent = node2
#             if node1.rank == node2.rank:
#                 node2.rank += 1