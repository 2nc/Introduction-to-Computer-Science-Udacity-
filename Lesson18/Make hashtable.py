# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    index = []
    i = 0
    while i < nbuckets:
        index.append([])
        i = i + 1
    return index

