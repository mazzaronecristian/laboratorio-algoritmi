import time
import timeit
import random as rand
import disjointSet as ds


#* disjointSetTests.test_union_set_performance() testa le performance dell'operazione di unione degli insiemi 
#* disgiunti implementati con liste concatenate (con e senza euristica dei pesi) e con le foreste con riduzione dei cammini;
#* ritorna tre liste di tempi di esecuzione medi per ogni dimensione di insieme testata e per ogni implementazione
#* di insieme disgiunto

def test_union_set_performance(sizes):

    list_times = []
    euristic_list_times = []
    forest_times = []

    for i in range( len( sizes ) ):
        list_times.append(0)
        euristic_list_times.append(0)
        forest_times.append(0)
        print("testing size: ", sizes[i])
        for z in range(10):
            list_time, euristic_list_time, forest_time = union_set( sizes[i] )
            
            list_times[i] += list_time
            euristic_list_times[i] += euristic_list_time
            forest_times[i] += forest_time

        list_times[i] /= 10
        euristic_list_times[i] /= 10
        forest_times[i] /= 10

    return {"linked list": list_times, "euristic linked list": euristic_list_times, "disjoint forest": forest_times}

def union_set(size):

    disjoiont_set_euristic = ds.DisjointSetLinkedList()
    disjoint_set_linked_list = ds.DisjointSetLinkedList()
    disjoint_set_forest = ds.DisjointSetForest()

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

    return list_time,euristic_list_time, forest_time


def test_connected_components_performance(graphs):
    
    list_times = []
    euristic_list_times = []
    forest_times = []

    for i in range( len ( graphs ) ):
        node_number = len( graphs[i].nodes )

        print("number of nodes: ", node_number)
        disjoint_set = ds.DisjointSetLinkedList()
        start_time = time.time()
        connected_components( graphs[i], disjoint_set )
        end_time = time.time()

        list_times.append( end_time - start_time )

        disjoint_set = ds.DisjointSetLinkedList()
        start_time = time.time()
        connected_components( graphs[i], disjoint_set, True )
        end_time = time.time()

        euristic_list_times.append( end_time - start_time )

        disjoint_set = ds.DisjointSetForest()
        start_time = time.time()
        connected_components( graphs[i], disjoint_set )
        end_time = time.time()

        forest_times.append( end_time - start_time )
    
    return {"linked list": list_times, "euristic linked list": euristic_list_times, "disjoint forest": forest_times}


#* ritorna le componenti connesse di un grafo non orientato
def connected_components(graph, disjoint_set, euristic=False):
    for node in graph.nodes:
        disjoint_set.make_set(node.value)
    
    for edge in graph.edges:
        node1 = edge[0]
        node2 = edge[1]  
        if euristic:  
            disjoint_set.euristic_union(node1.value, node2.value)
        else:
            disjoint_set.union(node1.value, node2.value)