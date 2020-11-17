'''
Project Algorithmic Thinking Part 01 - by USS.

Define three constants whose values are dictionaries corresponding to the 
three directed graphs shown in these linked diagrams:

http://storage.googleapis.com/codeskulptor-alg/alg_example_graph0.jpg
http://storage.googleapis.com/codeskulptor-alg/alg_example_graph1.jpg
http://storage.googleapis.com/codeskulptor-alg/alg_example_graph2.jpg

'''
EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}


def make_complete_graph(num_nodes):
    '''
    Input: 
        Number of nodes num_nodes 
    Return: 
        A dictionary corresponding to a complete directed graph with the 
    specified number of nodes. A complete graph contains all possible edges 
    subject to the restriction that self-loops are not allowed. The nodes of 
    the graph should be numbered num_nodes - 1 when num_nodes is positive. 
    Otherwise, the function returns a dictionary corresponding to the empty graph.
    '''

    complete_graph = {}
    digraph = range(num_nodes)

    for node in digraph:
        complete_graph[node] = set([])
        for to_the_other_node in digraph:
            if node != to_the_other_node:      
                complete_graph[node].add(to_the_other_node)

    return complete_graph