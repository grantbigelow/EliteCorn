from functools import reduce
import operator

class CornAnalyzer:
    def __init__(self,grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.results = []
        self.already_added = set()
        self.neighbor_dict = {}
    
    def check_corn(self, i, j):
        current = self.grid[i][j]
        
        #find neighbors in all directions from current corn stalk
        neighbors = {
            'right': [self.grid[i][k] for k in range(j +1, self.cols)],
            'left': [self.grid[i][k] for k in range(j)],
            'top': [self.grid[k][j] for k in range(i)],
            'bottom':[self.grid[k][j] for k in range(i+1, self.rows)]
        }
        self.neighbor_dict[(i,j)] = []

        #check if current corn is visible from outside the corn field
        for direction in neighbors:
            if all(current > neighbor for neighbor in neighbors[direction]) and (i,j) not in self.already_added:
                self.already_added.add((i,j))
                self.results.append(current)
                break
        #adds number of plants smaller than current corn in each direction
        for direction in neighbors:
            smaller_corn = sum(1 for neighbor in neighbors[direction] if current > neighbor)
            self.neighbor_dict[(i,j)].append(smaller_corn)
        
    def check_neighbors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "\n":
                    continue
                self.check_corn(i,j)  
        return self.results

def main():
    with open("input.txt", "r") as f:
        input_string = f.read().strip()
    
    grid = [list(map(int, line.strip())) for line in input_string.split('\n') if line.strip()]
    corn_grid = CornAnalyzer(grid)
    corn_grid.check_neighbors()
    

    elite_corn_num = 0
    elite_corn = ()
    for corn_stalk in corn_grid.neighbor_dict:
        if elite_corn_num < reduce(operator.mul,corn_grid.neighbor_dict[corn_stalk]):
            elite_corn_num = reduce(operator.mul,corn_grid.neighbor_dict[corn_stalk])
            elite_corn = corn_stalk
    print('Total number of visible corn from outside the field:', len(corn_grid.results))
    print("Elite Corn Spot:", elite_corn)
    print("Elite Corn Score:",elite_corn_num)
    print("Number of plants viewable from Elite Corn:")
    print("Right:",corn_grid.neighbor_dict[elite_corn][0],
          "Left:",corn_grid.neighbor_dict[elite_corn][1],
          "Top:",corn_grid.neighbor_dict[elite_corn][2],
          "Bottom:",corn_grid.neighbor_dict[elite_corn][3])

# Using the special variable 
# __name__
if __name__=="__main__":
    main()