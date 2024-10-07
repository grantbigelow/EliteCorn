import unittest
from functools import reduce
import operator
from corn import CornAnalyzer

class TestCornAnalyzer(unittest.TestCase):
    #This method will run before each test
    def setUp(self):
        self.input_string = '''41484
                               36623
                               76443
                               44650
                               46401'''
        self.grid = [list(map(int, line.strip())) for line in self.input_string.split('\n') if line.strip()]
        self.corn_grid = CornAnalyzer(self.grid)
    
    def test_viewable_corn(self):
        results = self.corn_grid.check_neighbors()
        expected_results = [4, 1, 4, 8, 4, 3, 6, 6, 3, 7, 6, 4, 3, 4, 6, 5, 0, 4, 6, 4, 0, 1]
        self.assertEqual(results, expected_results)
    
    def test_find_elite_corn(self):
        self.corn_grid.check_neighbors()
        elite_corn_num = 0
        elite_corn = ()
        for corn in self.corn_grid.neighbor_dict:
            score = reduce(operator.mul,self.corn_grid.neighbor_dict[corn])
            if elite_corn_num < score:
                elite_corn_num = score
                elite_corn = corn
        expected_elite_corn = (3,2)
        expected_elite_corn_num = 8
        self.assertEqual(elite_corn,expected_elite_corn)
        self.assertEqual(elite_corn_num,expected_elite_corn_num)
    
    def test_num_viewable_corn(self):
        self.corn_grid.check_neighbors()
        self.assertEqual(len(self.corn_grid.results),22)
    
    def test_elite_corn_details(self):
        self.corn_grid.check_neighbors()
        elite_corn_num=0
        elite_corn = ()
        for corn in self.corn_grid.neighbor_dict:
            score =reduce(operator.mul,self.corn_grid.neighbor_dict[corn])
            if elite_corn_num < score:
                elite_corn_num = score
                elite_corn = corn
        self.assertEqual(self.grid[elite_corn[0]][elite_corn[1]],6)
        self.assertEqual(self.corn_grid.neighbor_dict[elite_corn],[2,2,2,1])
    
    #negative tests
    def test_invalid_grid(self):
        #test invalid input data
        self.input_string = '''41a84
                               36623
                               76443
                               44650
                               46401'''
        with self.assertRaises(ValueError):
            invalid_grid = [list(map(int, line.strip())) for line in self.input_string.split('\n') if line.strip()]
            CornAnalyzer(invalid_grid)
    

    def test_incorrect_elite_corn_details(self):
        #test with incorrect height and amount of viewable plants
        self.corn_grid.check_neighbors()
        elite_corn_num=0
        elite_corn = ()
        for corn in self.corn_grid.neighbor_dict:
            score =reduce(operator.mul,self.corn_grid.neighbor_dict[corn])
            if elite_corn_num < score:
                elite_corn_num = score
                elite_corn = corn
        self.assertNotEqual(self.grid[elite_corn[0]][elite_corn[1]],5)
        self.assertNotEqual(self.corn_grid.neighbor_dict[elite_corn],[1,1,1,1])
if __name__ == "__main__":
    unittest.main()