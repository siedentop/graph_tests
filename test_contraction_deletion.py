# encoding: utf-8

import unittest
from contraction_deletion import *
import networkx as nx

class TestGraphPolynomial(unittest.TestCase):
    def test_BipartiteConnected(self):
        ''' Check the number of possible combinations of the bipartite graph
        with 2 nodes in each set. The combinations are all combinations such
        that graph stays connected.
        This is achieved by calculating the value of the Tutte polynomial at
        (1, 2).
        '''
        G = nx.Graph()
        G.add_nodes_from([1,2], bipartite=0) # Add the node attribute "bipartite"
        G.add_nodes_from(['a','b'], bipartite=1)
        G.add_edges_from([(1,'a'), (1,'b'),
                          (2,'a'), (2,'b')])
        result = tuttePolynomial(G, (1,2))
        self.assertEqual(result, 5)
    
    def test_contract(self):
        G = nx.MultiGraph()
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(1, 3)
        contract(G, (1,2))
        resultG = nx.Graph()
        G.add_edge(1, 2)
        G.add_edge(1, 2)
        self.assertTrue( nx.is_isomorphic(G, resultG) )

        
        # Contract with a double link already present
        H = nx.MultiGraph()
        H.add_edge(1, 2)
        H.add_edge(1, 2)
        contract(H, (1, 2))
        
        resultH = nx.MultiGraph()
        resultH.add_edge(1, 1)
        
        self.assertTrue( nx.is_isomorphic(H, resultH) )
        
if __name__=='__main__':
    unittest.main()
