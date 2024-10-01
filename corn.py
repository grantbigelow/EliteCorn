def check_corn(grid):
    rows = len(grid)
    cols = len(grid[0])

    results = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "\n":
                continue

            current = grid[i][j]
            right_neighbors = []
            left_neighbors = []
            already_added = []
            top_neighbors = []
            bottom_neighbors = []

            if ((i == 0 or i == rows)or (j==0 or j==cols)) and (i,j) not in already_added:
                already_added.append((i,j))
                results.append(current)
            
            #collect right neighbors
            for k in range(j+1, cols):
                right_neighbors.append(grid[i][k])
            #check if current number is bigger than all its right neighbors
            if all(current > neighbor for neighbor in right_neighbors) and (i,j) not in already_added:
                already_added.append((i,j))
                results.append(current)
            
            #collect left neighbors
            for k in range(j):
                left_neighbors.append(grid[i][k])
            #check if current number is bigger than all its left neighbors
            if all(current > neighbor for neighbor in left_neighbors) and (i,j) not in already_added:
                already_added.append((i,j))
                results.append(current)

            #collect top neighbors
            for k in range(j):
                top_neighbors.append(grid[i][k])
            #check if current number is bigger than all its top neighbors
            if all(current > neighbor for neighbor in top_neighbors) and (i,j) not in already_added:
                already_added.append((i,j))
                results.append(current)

            #collect bottom neighbors
            for k in range(j+1, rows):
                bottom_neighbors.append(grid[k][j])
            #check if current number is bigger than all its right neighbors
            if all(current > neighbor for neighbor in bottom_neighbors) and (i,j) not in already_added:
                already_added.append((i,j))
                results.append(current)
    return results
def main():
    f = open("input.txt", "r")
    corn_row = []
    left_side = []
    right_side = []
    input_string = '''41484
36623
76443
44650
46401'''

    grid = [list(map(int, line.strip())) for line in input_string.strip().split('\n')]
    print('Visible Corn:', check_corn(grid))
    print('Total Number of Visible Corn:', len(check_corn(grid)))
    # for row in f.readlines():
    #     corn_row.append(row.replace("\n", ""))
    #     left_side.append(row[0])
    #     right_side.append(row[-2])
    # first_row = corn_row[0]
    # last_row = corn_row[-1]
    # print('corn', right_side, left_side)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()