if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n, m = list(map(int, input().split()))
        distances = [-1]*(n)
        nodes = list(range(1, n+1))
        edges = []
        for edge in range(m):
            edges.append(tuple(map(int, input().split())))
        edges = set(edges)
        start = int(input())
        visited = set()
        nodes_to_visit = [[start]]
        multiplier = 0

        while nodes_to_visit:
            visiting_nodes = nodes_to_visit.pop(0)
            new_nodes = set()
            for current_node in visiting_nodes:
                visited.add(current_node)
                connected_edges = set([edge for edge in edges if current_node in edge])
                new_nodes.update(set([node for edge in connected_edges for node in edge if node not in visited]))
                edges = set([edge for edge in edges if edge not in connected_edges])
                distances[current_node-1] = 6*multiplier

            if len(new_nodes) != 0:
                nodes_to_visit.append(new_nodes-visited)
            multiplier += 1


        del(distances[start-1])
        print(" ".join(map(str, distances)))
