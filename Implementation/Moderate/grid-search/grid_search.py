if __name__ == "__main__":
    t = int(input())
    for test_case in range(t):
        R, C = list(map(int, input().split()))
        G = []
        P = []
        for row in range(R):
            G.append(input())
        r, c  = list(map(int, input().split()))
        for p_row in range(r):
            P.append(input())

        solution = "YES"

        for outer_row in range(R):
            for letter in range(len(G[outer_row])):
                if G[outer_row][letter:].find(P[0]) == 0:
                    solution = "YES"
                    for inner_row in range(1, r):
                        if G[outer_row+inner_row][letter:].find(P[inner_row]) != 0:
                            solution = "NO"
                            break

        print(solution)            