import time
import random as rand
import matplotlib.pyplot as plt

import disjointSetForest as dsf
import disjointSetLinkedList as dsl

def test_union_performance():
    disjoiont_set_forest = dsf.DisjointSetForest()
    disjoint_set_linked_list = dsl.DisjointSetLinkedList()

    sizes = [100, 1000, 10000, 100000]  # Dimensioni degli insiemi da testare
    list_times = []
    forest_times = []

    for size in sizes:
        data = list(range(size))

        rand.shuffle(data)

        for value in data:
            disjoint_set_linked_list.make_set(value)
            disjoiont_set_forest.make_set(value)
        
        #* unione senza euristica insiemi disgiunti con liste concatenate
        start_time = time.time()
        for i in range(size - 1):
            disjoint_set_linked_list.union(data[i], data[i + 1])
        end_time = time.time()

        list_times.append(end_time - start_time)

        #* unione senza euristica insiemi disgiunti con foreste
        start_time = time.time()
        for i in range(size - 1):
            disjoiont_set_forest.union(data[i], data[i + 1])
        end_time = time.time()

        forest_times.append(end_time - start_time)

        # crea un grafico con pyplot per visualizzare i tempi di esecuzione all'interno di list_times e forest_times, aggiungi una legenda
        plt.plot(sizes, list_times, label="List")
        plt.plot(sizes, forest_times, label="Forest")

test_union_performance()
