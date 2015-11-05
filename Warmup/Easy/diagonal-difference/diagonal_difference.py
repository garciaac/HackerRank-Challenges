if __name__ == "__main__":
    n = int(input())
    f, b = 0, 0
    for ii in range(n):
        line = list(map(int, input().split()))
        f += line[ii]
        b += line[n-1-ii]
    print(abs(f-b))