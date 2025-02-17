from collections import defaultdict, deque

import networkx as nx

import numpy as np


def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position



def nx_to_dict(graph):
    """
    Converts a NetworkX graph to a dictionary adjacency list.

    Parameters:
        graph (networkx.Graph): The NetworkX graph to convert.

    Returns:
        dict: A dictionary adjacency list representation of the graph.
    """
    adjacency_list = {node: list(graph.neighbors(node)) for node in graph.nodes()}
    return adjacency_list

def spanning_tree_algorithm(graph, start):

    # Initialize the spanning tree T
    T_vertices = set([start])  # Vertices in the tree
    T_edges = []  # Edges in the tree
    frontier = defaultdict(list)  # Tracks external connections for each vertex in T
    #print("START", start, graph[start])
    # Initialize frontier with neighbors of the start vertex
    for neighbor in graph[start]:
        frontier[start].append(neighbor)
    degrees = dict()

    neighbors = []
    #initializing dict that stores the remaining edges not in the tree
    for i in range(len(graph)):
        if i != start:
            degrees[i] = graph[i]

        neighbors.append([])
    #while we have not yet hit all nodes
    while len(T_vertices) < len(graph):
        # Classify vertices in T based on their frontier

        W2, W1, W0 = [], [], []
        for u in T_vertices:

            #neighbors of the nodes in the tree
            neighbors_outside = [v for v in frontier[u] if v not in T_vertices]
            neighbors[u] = neighbors_outside
            if len(neighbors_outside) >= 2:  #if there are more than 1 neighbours - it is well connected

                W2.append(u)
            elif len(neighbors_outside) == 1: #if u only has 1 neighbour, but that neighbour's neighbour is well connected
                v = neighbors_outside[0]
                if len([w for w in graph[v] if w in T_vertices]) >= 2:
                    #insertionSort(W1 + [u])
                    W1.append(u)

                else:   #if it needs to be a leaf
                    W0.append(u)

        #need to sort w2 and w1 based on the degree of the vertices.
        #sorting W2 in order of how well connected the node is
        for x in range(1, len(W2)):
            #neighbors_outside = [v for v in frontier[x] if v not in T_vertices]
            key_ind = W2[x]
            key = len(neighbors[W2[x]])  # Store the current element as the key to be inserted in the right position
            j = x - 1
            while j >= 0 and key < len(neighbors[W2[j]]):  # Move elements greater than key one position ahead
                    W2[j+1] = W2[j]
                    #arr[j + 1] = arr[j]  # Shift elements to the right
                    j -= 1
            W2[j + 1] = key_ind   # Insert the key in the correct position

        # print("CURRENT W2", W2)
        #
        # if len(W2) > 0:
        #     max2 = len(neighbors[W2[-1]])
        #     maxind, max_x = 0, 0
        #     x = len(W2)-1
        #     choice = x
        #     #if there are multiple nodes with the same degree, we choose the node whose neighbor has the nighest degree
        #
        #     while len(neighbors[W2[x]]) >= max2 and x>=0 and len(W2) > 1:
        #         print("Iterating through the neighbors of ", W2[x], neighbors[W2[x]], W2)
        #         max_k = 0
        #         #iterating through the neighbors of x
        #
        #         for k in neighbors[W2[x]]:
        #
        #             n_k = k
        #             neighbors[n_k] = [v for v in degrees[n_k] if v not in T_vertices]
        #             print("new k", n_k, neighbors[n_k])
        #             #W2_k = [0] * len(neighbors[W2[x]])
        #             #for neighbor k, we iterate through the neighbors and find the max, which we store in W2_k
        #             max_ = 0 #max degree of ks neighbors
        #
        #             # for l in neighbors[n_k]:
        #             #     #n_l = n_k[l] #lth neighbor of the kth neighbor of x
        #             #     neighbors[l] = [v for v in degrees[l] if v not in T_vertices and v != x]
        #             #     #key_l = len(neighbors[n_l])  # Store the current element as the key to be inserted in the right position
        #             #     # w1_neighbors[W1[x]] = len(neighbors[n_x])
        #             #
        #             #     if(max_ < len(neighbors[l])):
        #             #         maxind = k
        #             #         print("largest deg so farL", l, neighbors[l], "max within l", max_, "max k",
        #             #               max_k, "maximum in W2", max_x)
        #             #         max_ = len(neighbors[l])
        #             #
        #             #         # arr[j + 1] = arr[j]  # Shift elements to the right
        #             #
        #             if len(neighbors[k]) > max_k:  # Insert the key in the correct position
        #                 max_k = len(neighbors[k])
        #
        #
        #         x-=1
        #         if max_x < max_k:
        #             max_x = max_k
        #             choice = W2[x+1]
        #             print("choice", choice, max_k, W2[x+1], k)
        #
        #     if choice in W2:
        #         W2[-1] = choice
        #     print("W2", W2)


        #if there are no well connected nodes available
        #arranges W1 based on how well connected the neighbor of the neighbor of u is
        for x in range(1, len(W1)):
                #neighbors_outside = [v for v in frontier[x] if v not in T_vertices]
                key_ind = W1[x]
                n_x = neighbors[W1[x]][0]
                neighbors[n_x] = [v for v in degrees[n_x] if v not in T_vertices]
                print(W1[x], n_x, neighbors[n_x])
                key = len(neighbors[n_x])  # Store the current element as the key to be inserted in the right position
                #w1_neighbors[W1[x]] = len(neighbors[n_x])
                j = x - 1
                while j >= 0 and key < len([v for v in degrees[neighbors[W1[j]][0]] if v not in T_vertices]):  # Move elements greater than key one position ahead
                        W1[j+1] = W1[j]
                        #arr[j + 1] = arr[j]  # Shift elements to the right
                        j -= 1
                W1[j + 1] = key_ind  # Insert the key in the correct position
            #print(w1_neighbors)
        # for i in range(len(graph)):
        #         if len(neighbors[i]) > 0:
        #             print(i,":", len(neighbors[i]))
        #
        # for x in range(len(W2)):
        #     print("-----------------------------------------")
        #     print(W2[x], len(neighbors[W2[x]]), neighbors[W2[x]])
        #
        # if W1:
        #     print("W1--", W1, W1[-1])
        #
        # print("new iter")

        # Choose vertex u for expansion
        if W2:
            u = W2[-1]
            for j in degrees:
                # if j == u:
                #     degrees[j] = []
                if u in degrees[j]:
                    degrees[j].remove(u)

        elif W1:
            u = W1[-1]
            for j in degrees:
                # if j == u:
                #     degrees[j] = []
                if u in degrees[j]:
                    degrees[j].remove(u)
                    
        else:
            u = W0.pop()
            for j in degrees:
                # if j == u:
                #     degrees[j] = []
                if u in degrees[j]:
                    degrees[j].remove(u)

        # Expand T at u
        neighbors_outside = [v for v in frontier[u] if v not in T_vertices]
        for v in neighbors_outside:
            T_edges.append((u, v))
            T_vertices.add(v)
            # Update the frontier for the new vertex v
            for w in graph[v]:
                if w not in T_vertices:
                    frontier[v].append(w)
        print("CHOSEN:", u)

        #print(degrees)

    return T_edges
#
# n = 50
# p = 1
# k = 10
# g = nx.watts_strogatz_graph(n, k, p)
# m = 2000
# g = nx.random_shell_graph([(10, 20, 0.8), (20, 40, 0.8), (20, 40, 0.9)])
#
# # g = nx.random_shell_graph([(10, 20, 0.8), (20, 40, 0.8)])
#
# dg = nx_to_dict(g)
#
# G = nx.Graph()
# lengths = []
#
# for u in range(0, n):
#     lengths.append(len(dg[u]))
#     for v in dg[u]:
#         G.add_edge(u, v)
# nx.draw(G, with_labels=True, edge_color='lightblue')
#
# print(dg)
# print(1 in dg.keys())
# start_vertex = (int)(np.argmax(lengths))  # Starting vertex
# tree_edges = spanning_tree_algorithm(dg, start_vertex)
# print("Edges in the spanning tree:", tree_edges)
# tree = nx.Graph()
# leaves = 0
# freq = {}
# for i in range(0, n):
#     freq[i] = 0
#
# for edge in tree_edges:
#         u, v = edge
#         tree.add_edge(u, v)
#         freq[u]+=1
#         freq[v]+=1
#
# for i in range(n):
#         if freq[i] == 1:
#             leaves+=1
#             print(i)
#
# print("number of leaves =", leaves)


