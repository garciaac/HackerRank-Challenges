if __name__ == '__main__':
    nt = list(map(int, input().split()))
    n = nt[0]
    t = nt[1]
    width = list(map(int, input().split()))
    
    for outer in range(t):
        ij = list(map(int, input().split()))
        i = ij[0]
        j = ij[1]
        widestPoint = 3
        for inner in range(i, j+1):
            if width[inner] < widestPoint:
                widestPoint = width[inner]
        print(widestPoint)