import disjointSetTests
import graph
import node
import plot as plt
import random as rand

node_number = [50, 100, 200, 1000, 5000, 10000, 50000, 100000, 200000]           #* Dimensioni degli insiemi da testare


#* test sulle performance di unione di insiemi disgiunti
# times = disjointSetTests.test_union_set_performance( node_number )

# plt.plot_results( node_number, list( times.values() ),
#                  list( times.keys() ),
#                 "Unione di insiemi disgiunti",
#                 "images/union_performace.png")


#* test sulle performance di ricerca di componenti connesse
graphs = []
#genera un numero casuale compreso tra 1 e 5 usando la libreria random

edge_number = [2 * x for x in node_number]                        #* Numero di archi da testare

for i in range( len(node_number) ):
    nodes = node.random_nodes( node_number[i] )
    graphs.append( graph.random_graph( nodes, edge_number[i] ) )  

times = disjointSetTests.test_connected_components_performance( graphs )

plt.plot_results( node_number, list( times.values() ),
                list( times.keys() ),
                "Ricerca di componenti connesse",
                "images/connected_components_performance.png",
                "n of nodes (N)" )