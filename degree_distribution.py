"""
EX_GRAPH0, EX_GRAPH1, EX_GRAPH2 - Define three constants whose values are dictionaries 
corresponding to the three directed graphs shown below. The graphs are numbered 0, 1, and 2, 
respectively, from left to right
"""
#EX_GRAPH0 = {'cat':set(['dog','banana']), 'dog':set([]), 'banana':set([])}
EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 
				5:set([2]),6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2, 6]), 2:set([3,7]),3:set([7]), 4:set([1]), 
				5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
	"""
	make_complete_graph(num_nodes) - Takes the number of nodes num_nodes and returns a 
	dictionary corresponding to a complete directed graph with the specified number of nodes. 
	"""
	graph = {}
	if num_nodes <= 0:
		return graph
	else:
		for node in range(num_nodes):
			nlist=range(num_nodes)
			nlist.remove(node)
			graph[node]=set(nlist)
		return graph
#print make_complete_graph(5)

def compute_in_degrees(digraph):
	"""
	compute_in_degrees(digraph) - Takes a directed graph digraph (represented as a dictionary) 
	and computes the in-degrees for the nodes in the graph. The function should return a 
	dictionary with the same set of keys (nodes) as digraph whose corresponding values are the 
	number of edges whose head matches a particular node.
	"""
	in_degree_graph = {}
	for key in digraph.keys():
		in_degree_graph [key] =[]
		counter = 0
		#print 'key is', key
		for value in digraph.values():
			#print 'value is', value
			if key in value:
				counter += 1
				#print 'match found, counter is', counter
		in_degree_graph[key] = counter
	return in_degree_graph
#print compute_in_degrees(EX_GRAPH2)


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
#print in_degree_distribution(EX_GRAPH2)








