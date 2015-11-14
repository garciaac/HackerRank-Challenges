#Refactor this

class Edge:
    def __init__(self, metadata):
        self.nodeA, self.nodeB, self.weight = metadata.split()
        self.weight = int(self.weight)
    def __lt__(self, other):
        return self.weight < other.weight
    def __add__(self, other):
        return self.weight + other.weight
    def __rad__(self, other):
        return self + other

if __name__ == "__main__":
    v, e = list(map(int, input().split()))
    edges = []
    vertices = set()
    for ii in range(1, v+1):
        vertices.add(str(ii))
    for ii in range(e):
        edges.append(Edge(input()))
    edges = sorted(edges)
    start = input()
    
    included_vertices = set()
    vertices.remove(start)
    answer = 0
    
    while not len(vertices) == 0:
        for edge in edges:
            if edge.nodeA not in vertices and edge.nodeB not in vertices:
                del(edge)
            elif edge.nodeA in vertices and edge.nodeB in vertices:
                continue
            else:
                answer += edge.weight
                included_vertices.add(edge.nodeA)
                included_vertices.add(edge.nodeB)
                if edge.nodeA in vertices:
                    vertices.remove(edge.nodeA)
                if edge.nodeB in vertices:
                    vertices.remove(edge.nodeB)
                break
                    
    print(answer)