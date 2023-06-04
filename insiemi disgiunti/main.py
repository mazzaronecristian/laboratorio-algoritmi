import disjointSetTests
import matplotlib.pyplot as plt

def plot_results(x, y, labels):
    for i in range(len(y)):
        plt.plot(x, y[i], label=labels[i])
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.legend()
    plt.savefig('images/plot.png', format="png", dpi=300)
    plt.show()
    plt.draw()

node_number = [10, 20, 50, 100, 200, 1000, 5000, 10000]           #* Dimensioni degli insiemi da testare

#* disjointSetTests.test_union_set_performance() testa le performance dell'operazione di unione degli insiemi 
#* disgiunti implementati con liste concatenate (con e senza euristica dei pesi) e con le foreste (con e senza euristica dei pesi)
#* ritorna una tre liste di tempi di esecuzione medi per ogni dimensione di insieme testata e per ogni implementazione
#* di insieme disgiunto

edge_number = [2 * x for x in node_number]


times = disjointSetTests.test_union_set_performance( node_number )

plot_results( node_number, list( times.values() ), list( times.keys() ) )
