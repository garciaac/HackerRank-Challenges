def isCavity(grid, x, y):
    return (    grid[x][y] > grid[x-1][y] 
            and grid[x][y] > grid[x+1][y] 
            and grid[x][y] > grid[x][y-1] 
            and grid[x][y] > grid[x][y+1])

def buildGrid(n):
    grid = []
    for rows in range(n):
        grid.append(list(input().strip()))
    return grid

if __name__ == "__main__":
    n = int(input().strip())
    grid = buildGrid(n)
    print("".join(grid[0]))
    if n == 1:
        pass
    else:
        for x in range(1, len(grid)-1):
            for y in range(1, len(grid)-1):
                if isCavity(grid, x, y):
                    grid[x][y] = "X"
            print("".join(grid[x]))
        print("".join(grid[len(grid)-1]))
