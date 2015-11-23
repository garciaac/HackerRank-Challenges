###############################################################
# This solution works, but it sucks
###############################################################

def negate(point):
    return -point

def translate(i,j,points):
    points[i:j] = list(map(negate, points[i:j]))


if __name__ == "__main__":
    n = int(input())
    x, y = [], []
    for ii in range(n):
        temp = list(map(int, input().split()))
        x.append(temp[0])
        y.append(temp[1])
    
    q = int(input())
    for ii in range(q):
        operation, i, j = input().split()
        i, j = int(i), int(j)
    
        i -= 1
    
        if operation == "X":
            translate(i,j,y)
        elif operation == "Y":
            translate(i,j,x)
        else:
            quadrants = [0,0,0,0]
            
            for ii in range(i, j):
                if x[ii] > 0 and y[ii] > 0:
                    quadrants[0] += 1
                elif x[ii] < 0 and y[ii] > 0:
                    quadrants[1] += 1
                elif x[ii] < 0 and y[ii] < 0:
                    quadrants[2] += 1
                else:
                    quadrants[3] += 1

            print(" ".join(map(str, quadrants)))