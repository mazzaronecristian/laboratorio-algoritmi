import time
import timeit
import random as rand

import disjointSetForest as dsf
import disjointSetLinkedList as dsl


def test_union_performance(sizes):
    disjoiont_set_euristic = dsl.DisjointSetLinkedList()
    disjoint_set_linked_list = dsl.DisjointSetLinkedList()
    disjoint_set_forest = dsf.DisjointSetForest()

    list_times = []
    euristic_list_times = []
    forest_times = []

    for i in range(len(sizes)):
        list_times.append(0)
        euristic_list_times.append(0)
        forest_times.append(0)
        for z in range(10):
            list_time, euristic_list_time, forest_time = test_body(disjoint_set_linked_list, 
                                                                    disjoiont_set_euristic, 
                                                                    disjoint_set_forest, sizes[i])
            
            list_times[i] += list_time
            euristic_list_times[i] += euristic_list_time
            forest_times[i] += forest_time

        list_times[i] /= 10
        euristic_list_times[i] /= 10
        forest_times[i] /= 10

    return {"linked list": list_times, "euristic linked list": euristic_list_times, "disjoint forest": forest_times}

def test_body(disjoint_set_linked_list, disjoiont_set_euristic, disjoint_set_forest, size):
    data = list(range(size))

    rand.shuffle(data)

    for value in data:
        disjoint_set_linked_list.make_set(value)
        disjoiont_set_euristic.make_set(value)
        disjoint_set_forest.make_set(value)

    #* unione senza euristica insiemi disgiunti con liste concatenate
    start_time = time.time()
    for i in range(size-1):
        random_index1 = rand.randint(i+1, size-1)
        random_index2 = rand.randint(i+1, size-1)
        disjoint_set_linked_list.union(data[random_index1], data[random_index2])
    end_time = time.time()
    list_time = end_time - start_time

    #* unione con euristica insiemi disgiunti con liste concatenate
    start_time = time.time()
    for i in range(size-1):
        random_index1 = rand.randint(i+1, size-1)
        random_index2 = rand.randint(i+1, size-1)
        disjoiont_set_euristic.euristic_union(data[random_index1], data[random_index2])
    end_time = time.time()
    euristic_list_time = end_time - start_time

    #* unione di insiemi disgiunti con foreste con riduzione dei cammini
    start_time = time.time()
    for i in range(size-1):
        random_index1 = rand.randint(i+1, size-1)
        random_index2 = rand.randint(i+1, size-1)
        disjoint_set_forest.union(data[random_index1], data[random_index2])
    end_time = time.time()
    forest_time = end_time - start_time

    return list_time, euristic_list_time, forest_time


