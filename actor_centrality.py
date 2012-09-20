"""Utility Functions:"""

import time
import random
import heapq
from operator import itemgetter

"""creating a graph in the form of a dictionary
G[node1][node2] = {} denotes an edge between node1 and node2"""
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

"""calculates average centrality for a given node"""
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while open_list:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return (float(sum(distance_from_start.values())))/len(distance_from_start)




"""reading the imdb file"""
fh = open('imdb1.tsv', "r")

G = {}
actors = {}
    
for line in fh.readlines():
    (actor, film, year) = line.split("\t")
    make_link(G, actor, film)
    actors[actor] = True

"""outputs the top k most central actors in the imdb network"""
def top_central_actors(G, k):
    start = time.clock()
    scores = {}
    for a in actors:
        scores [a] = centrality(G, a)
    k_keys_sorted =  heapq.nsmallest(k, scores.items(), key = itemgetter(1))
    i = 1
    print k_keys_sorted
    
    for i in range(k):
        print i+1, ' - ', k_keys_sorted[i][0], '   centrality score: ', k_keys_sorted[i][1]
        i += 1
    
    end = time.clock()
    time_taken = end - start
    print 'time taken', time_taken
    
print top_central_actors(G, 20)




