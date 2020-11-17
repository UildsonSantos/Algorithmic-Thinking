'''
Unit tests for project 01 parte 01 (Degree distributions for graph), by USS.
'''

import unittest 

from Project_01 import compute_in_degrees
from Project_01 import in_degree_distribution
from Project_01 import EX_GRAPH0, EX_GRAPH1, EX_GRAPH2
from alg_module1_graphs import GRAPH0, GRAPH1, GRAPH2, GRAPH3, GRAPH4, GRAPH5, GRAPH6, GRAPH7, GRAPH8, GRAPH9


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.ex_graph0 = {0: set([]),
                          1: set([]),
                          2: set([])}

        

    def test_degrees(self):
        self.assertEqual(in_degree_distribution(self.ex_graph0), {0: 3})
        self.assertEqual(in_degree_distribution(EX_GRAPH0), {0: 1, 1: 2})
        self.assertEqual(in_degree_distribution(EX_GRAPH1), {1: 5, 2: 2})
        self.assertEqual(in_degree_distribution(EX_GRAPH2), {0: 2, 1: 1, 2: 3, 3: 4})
        self.assertEqual(in_degree_distribution(GRAPH0), {1: 4})
        self.assertEqual(in_degree_distribution(GRAPH1), {4: 1, 0: 4})
        self.assertEqual(in_degree_distribution(GRAPH2), {0: 1, 1: 4})
        self.assertEqual(in_degree_distribution(GRAPH3), {4: 5})
        self.assertEqual(in_degree_distribution(GRAPH4), {0: 1, 1: 3})
        self.assertEqual(in_degree_distribution(GRAPH5), {1: 2, 2: 2, 3: 2, 4: 2})
        self.assertEqual(in_degree_distribution(GRAPH6), {1: 1, 2: 6, 3: 1})
        self.assertEqual(in_degree_distribution(GRAPH7), {0: 7, 1: 2, 2: 1, 9: 2, 10: 1, 11: 1, 12: 1})
        self.assertEqual(in_degree_distribution(GRAPH8), {16: 1, 11: 1, 5: 1, 3: 1, 2: 3, 1: 4, 0: 9})
        self.assertEqual(in_degree_distribution(GRAPH9), {27: 1, 32: 2, 36: 1, 17: 1, 34: 1, 33: 1, 3: 5, 2: 8, 1: 6, 4: 3, 0: 21})


              
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)