# This is a sample Python script.
from igraph import *
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import sys
lines = []
input = open("all-hard.in", "r")
print(input)
#input = input.splitlines("\n")
for line in input:
    lines.append(line[0:len(line)-1])

print(lines)
graphs = []
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from MaxLeafSpanningTree import spanning_tree_algorithm


def igraph_to_dict(igraph_obj):

    adjacency_list = igraph_obj.get_adjlist()  # Get adjacency list from igraph
    graph_dict = {i: neighbors for i, neighbors in enumerate(adjacency_list)}

    return graph_dict


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


def input_to_dict():
    graph_no = 0
    i = 1
    while i < len(lines):
        n, m = lines[i].split()
        graph = dict()
        for k in range((int)(n)):
            graph[k] = list()
        #print(graph)

        for j in range(i+1, (int)(m) + i + 1):

            #print("line", lines[j])
            #print((int)(lines[j][0]),  (int)(lines[j][2]))
            u, v = lines[j].split()
            graph[(int)(u)].append((int)(v))
            graph[(int)(v)].append((int)(u))
            #print(graph)
        i += (int)(m) + 1
        #print("i", i)
        graphs.append(graph)
        graph_no+=1

#input_to_dict()
#print(graphs)
if __name__ == "__main__":

    #
    p = 1
    k = 10
    #print("GRAPHS:::", graphs)
    input_to_dict()
    print(graphs)
    print(len(graphs))
    #dg = graphs[0]
    m = 2000
    #g = Graph.Erdos_Renyi(n=n, p = 0.09)
    output = open("hard.out", "w")
    for dg in graphs:
        #g = nx.erdos_renyi_graph(n = 100, p = 0.4)#[(10, 20, 0.85), (20, 40, 0.8), (20, 40, 0.9), (30, 50, 0.85), (20, 60, 0.85)])
        n = len(dg)
        #print("shell")
        #dg = nx_to_dict(g)

        G = nx.Graph()
        lengths = []
        for u in range(0, n):
            lengths.append(len(dg[u]))
            for v in dg[u]:
                G.add_edge(u, v)

        nx.draw(G, with_labels=True, edge_color='lightblue')
        plt.show()
        plt.clf()
        #print(dg)

        start_vertex = (int)(np.argmax(lengths))  # Starting vertex
        tree_edges = spanning_tree_algorithm(dg, start_vertex)
        #print("Edges in the spanning tree:", tree_edges)
        tree = nx.Graph()
        leaves = 0
        freq = {}
        #The corresponding hard.out file should contain k solutions. The first line of each solution
        # contains two numbers s and ℓ, where s is the number of leaves on your solution and ℓ is the number
        # of edges on your tree. The next ℓ lines will contain each one edge consisting of two space separated
        # sorted numbers corresponding to the nodes id’s. Edges should appear lexicographically, from least
        # to largest.


        for i in range(0, n):
            freq[i] = 0
        edges = 0
        for edge in tree_edges:
            u, v = edge
            edges += 1
            tree.add_edge(u, v)
            freq[u]+=1
            freq[v]+=1

        for i in range(n):
            if freq[i] == 1:
                leaves += 1
                #print(i)

        if len(tree) == 0:
            output.write("" + (str)(leaves) + " " + (str)(edges) + "\n")
            continue

        print(leaves, edges)
        output.write(""+(str)(leaves)+" "+(str)(edges)+"\n")

        tree_dict = nx_to_dict(tree)
        for i in range(n):
            vs = sorted(tree_dict[i])
            for v in vs:
                if v > i:
                    print(i, v)
                    output.write("" + (str)(i) + " " + (str)(v) + "\n")




        nx.draw(tree, with_labels = True, edge_color='red')
        plt.show()
    # Create an igraph object
    # g_igraph = Graph(edges=[(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (4, 6)])

    # Convert igraph to networkx


