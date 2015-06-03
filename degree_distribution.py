"""
EX_GRAPH0, EX_GRAPH1, EX_GRAPH2 - Define three constants whose values are dictionaries 
corresponding to the three directed graphs shown below. The graphs are numbered 0, 1, and 2, 
respectively, from left to right
"""
#EX_GRAPH0 = {'cat':set([1,2]), 'dog':set([]), 'banana':set([])}
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
	for node in range(len(digraph)):
		#print 'node is', node
		nlist=range(len(digraph))
		nlist.remove(node)
		#print 'nlist is', nlist
		indegree=0
		for othernode in nlist:
			#print 'othernode is', digraph[othernode]
			if node in digraph[othernode]:
				indegree += 1
		in_degree_graph[node]=indegree
	return in_degree_graph
print compute_in_degrees(EX_GRAPH0)

def in_degree_distribution(digraph):
	"""
	in_degree_distribution(digraph) - Takes a directed graph digraph (represented as a 
	dictionary) and computes the unnormalized distribution of the in-degrees of the graph. 
	"""
	in_degree_graph = compute_in_degrees(digraph)
	#print in_degree_graph
	in_deg_destribute = {}
	for num_indegree in range(len(in_degree_graph)):
		#print 'num_indegree is here', num_indegree
		indeg_count=0
		for node in range(len(in_degree_graph)):
			if in_degree_graph[node] == num_indegree:
				#print "node is here", node
				indeg_count += 1
		if indeg_count > 0:
		#In-degrees with no corresponding nodes in the graph are not included
			in_deg_destribute [num_indegree] = indeg_count
		#print "in degree of", num_indegree," is", in_deg_destribute [num_indegree]
	return in_deg_destribute
print in_degree_distribution(EX_GRAPH0)








