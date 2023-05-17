import disjointSetLinkedList as dsll    # Import the disjoint set linked list module
import disjointSetForest as dsf         # Import the disjoint set forest module

# ds = dsll.DisjointSetLL()               # Create a new disjoint set linked list

# ds.make_set(1)                          # Create a new set with value 1
# ds.make_set(2)                          # Create a new set with value 2
# ds.make_set(3)                          # Create a new set with value 3

# ds.union(1, 2)                          # Union the sets with values 1 and 2
# ds.euristic_union(3, 2)                 # Union the sets with values 2 and 3

# print(ds.find_set(2).value)             # Find the representative of the set with value 1

# print(ds.find_set(4))                   # Find the representative of the set with value 2

dsf = dsf.DisjointSetForest()            # Create a new disjoint set forest

# crea 10 insiemi disgiunti 
for i in range(10):
    dsf.make_set(i)                          # Create a new set with value i

# unisci gli insieme disgiunti con valori 1 e 2 e 3 e 4 e 5 e 6 e 7 e 8 e 9
dsf.union(1, 2)                          # Union the sets with values 1 and 2
dsf.union(3, 4)                          # Union the sets with values 3 and 4
dsf.union(5, 6)                          # Union the sets with values 5 and 6
dsf.union(7, 8)                          # Union the sets with values 7 and 8

dsf.union(1, 3)                          # Union the sets with values 1 and 3
dsf.union(5, 2)                          # Union the sets with values 5 and 7

print(dsf.find_set(1).value)             # Find the representative of the set with value 1
