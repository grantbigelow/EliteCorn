from functools import reduce
import operator

class CornAnalyzer:
    def __init__(self,grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.results = []
        self.already_added = []
        self.neighbor_dict = {}
    
    def check_corn_direction(self, i, j, direction):
        current = self.grid[i][j]
        neighbors = []
        smaller_corn = 0
        if direction == "right":
            for k in range(j+1, self.cols):
                neighbors.append(self.grid[i][k])
        elif direction == "left":
            for k in range(j):
                neighbors.append(self.grid[i][k])
        elif direction == 'top':
            for k in range(i):
                neighbors.append(self.grid[k][j])
        elif direction == 'bottom':
            for k in range(i+1,self.rows):
                neighbors.append(self.grid[k][j])
        self.neighbor_dict[(i,j)] = [] if (i,j) not in self.neighbor_dict else self.neighbor_dict[(i,j)]
        if all(current > neighbor for neighbor in neighbors):
            if (i,j) not in self.already_added:
                self.already_added.append((i,j))
                self.results.append(current)
        
        for neighbor in neighbors:
            if current > neighbor:
                smaller_corn += 1
        
        self. neighbor_dict[(i,j)].append(smaller_corn)

    def check_neighbors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "\n":
                    continue

                #Check neighbors of inner-corn in all directions
                self.check_corn_direction(i,j,'right')
                self.check_corn_direction(i,j,'left')
                self.check_corn_direction(i,j,'top')
                self.check_corn_direction(i,j,'bottom')
        
        return self.results

def main():
    f = open("input.txt", "r")
    input_string = '''41484
36623
76443
44650
46401'''
    input= f.read()
    grid = [list(map(int, line.strip())) for line in input_string.strip().split('\n')]
    corn_grid = CornAnalyzer(grid)
    corn = corn_grid.check_neighbors()
    print('Total Number of Visible Corn:', len(corn))

    elite_corn_num = 0
    elite_corn = ()
    for corn_stalk in corn_grid.neighbor_dict:
        if elite_corn_num < reduce(operator.mul,corn_grid.neighbor_dict[corn_stalk]):
            elite_corn_num = reduce(operator.mul,corn_grid.neighbor_dict[corn_stalk])
            elite_corn = corn_stalk
    print("Elite Corn:", elite_corn, "Elite Corn Score:",elite_corn_num)
    print(corn_grid.neighbor_dict[elite_corn])

# Using the special variable 
# __name__
if __name__=="__main__":
    main()