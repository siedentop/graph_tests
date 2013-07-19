def tuttePolynomial(G, point):
    ''' Returns the value of the Tutte Polynomial evaluated at point.
    
    Implementation:
    --------------
    This is implemented through Deletion-Contraction algorithm.
    
    Parameters:
    -----------
    G : graph
        An undirected graph.
    
    point : Evaluation point of Tutte Polynomial
        (x, y) values of Tutte Polynomial
    
    Returns:
    -------
    Value of Tutte Polynomial.
    
    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Tutte_polynomial
    '''
    delete = set()
    contract = set()

def contract(graph, edge):
    ''' Contracts the graph at specified edge and returns new graph.
    graph needs to be a MultiGraph.'''
    if not graph.is_multigraph():
        raise TypeError('Graph needs to be a nx.MultiGraph.')
    (node1, node2) = edge
    new_node = 7 # Assert that 7 is new...
    for n in graph.neighbors_iter(node1):
        if n != node2:
            graph.add_edge(new_node, n)
    for n in graph.neighbors_iter(node2):
        if n != node1:
            graph.add_edge(new_node, n)
    graph.remove_node(node1)
    graph.remove_node(node2)
    #graph.remove_edge(new_node, new_node)