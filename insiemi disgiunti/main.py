import disjointSetTests
import matplotlib.pyplot as plt

def plot_results(x, y, labels):
    for i in range(len(y)):
        plt.plot(x, y[i], label=labels[i])
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.legend()
    plt.show()

sizes = [10, 20, 50, 100, 200, 1000, 5000, 10000, 100000, 200000]           #* Dimensioni degli insiemi da testare

#* unionTest.test_union_performance() testa le performance dell'operazione di unione degli insiemi 
#* disgiunti implementati con liste concatenate (con e senza euristica dei pesi) e con le foreste (con e senza euristica dei pesi)
#* ritorna una tre liste di tempi di esecuzione medi per ogni dimensione di insieme testata e per ogni implementazione
#* di insieme disgiunto

list_times = []
euristic_list_times = []

times = disjointSetTests.test_union_performance( sizes )  

plot_results( sizes, list( times.values() ), list( times.keys() ) )
