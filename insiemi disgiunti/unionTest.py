import time
import random as rand
import matplotlib.pyplot as plt

import disjointSetForest as dsf
import disjointSetLinkedList as dsl

def test_union_performance():
    disjoiont_set_euristic = dsl.DisjointSetLinkedList()
    disjoint_set_linked_list = dsl.DisjointSetLinkedList()

    sizes = [10, 20, 50, 100, 200, 1000, 5000, 10000]  # Dimensioni degli insiemi da testare
    list_times = []
    euristic_list_times = []

    for i in range(len(sizes)):
        list_times.append(0)
        euristic_list_times.append(0)
        for z in range(10):
            list_time, euristic_list_time = test_body(disjoint_set_linked_list, disjoiont_set_euristic, sizes[i])
            list_times[i] += list_time
            euristic_list_times[i] += euristic_list_time
        list_times[i] /= 10
        euristic_list_times[i] /= 10

    plot_results(sizes, [list_times, euristic_list_times], ["Linked list", "Euristic linked list"])

def test_body(disjoint_set_linked_list, disjoiont_set_euristic, size):
    data = list(range(size))

    rand.shuffle(data)

    for value in data:
        disjoint_set_linked_list.make_set(value)
        disjoiont_set_euristic.make_set(value)

    #* unione senza euristica insiemi disgiunti con liste concatenate
    print("unione non euristica in corso...")
    start_time = time.time()
    for i in range(size-1):
        random_index1 = rand.randint(i+1, size-1)
        random_index2 = rand.randint(i+1, size-1)
        disjoint_set_linked_list.union(data[random_index1], data[random_index2])
    end_time = time.time()
    list_time = end_time - start_time

    #* unione con euristica insiemi disgiunti con liste concatenate
    print("unione euristica in corso...")
    start_time = time.time()
    for i in range(size-1):
        random_index1 = rand.randint(i+1, size-1)
        random_index2 = rand.randint(i+1, size-1)
        disjoiont_set_euristic.euristic_union(data[random_index1], data[random_index2])
    end_time = time.time()
    euristic_list_time = end_time - start_time

    return list_time, euristic_list_time

def plot_results(x, y, labels):
    for i in range(len(y)):
        plt.plot(x, y[i], label=labels[i])
    plt.xlabel('n')
    plt.ylabel('time (s)')
    plt.legend()
    plt.show()

test_union_performance()
