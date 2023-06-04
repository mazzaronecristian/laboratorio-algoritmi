import disjointSetTests
import graph
import node
import plot as plt


node_number = [10, 20, 50, 100, 200, 1000, 5000, 10000]           #* Dimensioni degli insiemi da testare


edge_number = [2 * x for x in node_number]                        #* Numero di archi da testare

#* disjointSetTests.test_union_set_performance() testa le performance dell'operazione di unione degli insiemi 
#* disgiunti implementati con liste concatenate (con e senza euristica dei pesi) e con le foreste con riduzione dei cammini;
#* ritorna tre liste di tempi di esecuzione medi per ogni dimensione di insieme testata e per ogni implementazione
#* di insieme disgiunto

times = disjointSetTests.test_union_set_performance( node_number )

plt.plot_results( node_number, list( times.values() ),
                 list( times.keys() ),
                "Unione di insiemi disgiunti",
                "images/union_performace.png")

