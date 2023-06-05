import random as rand

class Graph:
    def __init__( self, nodes ):
        self.nodes = nodes
        self.edges = []

    def add_edge( self, node1, node2 ):
        self.edges.append( ( node1, node2 ) )

#* dato un array di nodi e un numero n, ritorna un grafo non orientato con n archi
def random_graph( nodes, edges_number ):
    graph = Graph( nodes )

    for i in range( edges_number ):
        random_index1 = rand.randint( 0, len( nodes )-1 )
        random_index2 = rand.randint( 0, len( nodes )-1 )
        if random_index1 != random_index2:
            graph.add_edge( nodes[ random_index1 ], nodes[ random_index2 ] )
        else:
            i -= 1

    return graph