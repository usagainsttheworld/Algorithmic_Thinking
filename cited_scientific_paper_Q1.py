"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)
#print "citation_graph is", citation_graph

def compute_in_degrees(digraph):
    """
    compute_in_degrees(digraph) - Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph. The function should return a 
    dictionary with the same set of keys (nodes) as digraph whose corresponding values are the 
    number of edges whose head matches a particular node.
    """
    in_degree_graph = {}
    print "in_degree loop starts"
    loopcount = 0
    for key in digraph.keys():
        print loopcount
        loopcount += 1
        in_degree_graph [key] =[]
        counter = 0
        for value in digraph.values():
            if key in value:
                counter += 1
        in_degree_graph[key] = counter
    print "in_degree loop ends"
    return in_degree_graph
#print "in-degree for nodes in graph are",compute_in_degrees(citation_graph)

def in_degree_distribution(digraph):
    """
    in_degree_distribution(digraph) - Takes a directed graph digraph (represented as a 
    dictionary) and computes the unnormalized distribution of the in-degrees of the graph. 
    """
    in_degree_graph = compute_in_degrees(digraph)
    destribute_graph = {}
    for value in in_degree_graph.values():
        if value not in destribute_graph:
            destribute_graph[value] = 1
        else:
            destribute_graph[value] +=1
    return destribute_graph
print "in-degree distribution are", in_degree_distribution(citation_graph)