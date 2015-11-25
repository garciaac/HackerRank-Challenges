import math

class SegmentNode:
    
    def __init__(self, value, start=None, end=None):
        self.value = value
        self.start = start
        self.end = end

    def __add__(self, other):
        if other is None:
            return self
        
        if self.start < other.start:
            start = self.start
        else:
            start = other.start
            
        if self.end > other.end:
            end = self.end
        else:
            end = other.end
        
        value = abs(self.value) + abs(other.value)
        return SegmentNode(value, start, end)
    
    def __radd__(self, other):
        return self + other
    
    def __str__(self):
        return str(self.value)

class SegmentTree:

    def __init__(self, data, node_type):
        self.tree = [None]*2*int(math.pow(2, math.ceil(math.log(len(data), 2))))
        self.data = data
        self.node_type = node_type
        self.build(0, len(data)-1, 0)
    
    def __str__(self):
        return str(list(map(str, self.tree)))
    
    def __len__(self):
        return len(self.tree)
    
    def build(self, start, end, current_index):
        if start == end:
            self.tree[current_index] = self.node_type(self.data[start], start, end)
            return self.tree[current_index]
        else:
            midpoint = int((start+end)/2)
            self.tree[current_index] = self.merge(self.build(start, midpoint, current_index*2+1),
                                                  self.build(midpoint+1, end, current_index*2+2))
            return self.tree[current_index]        
    
    def merge(self, left_node, right_node):
        return left_node + right_node
    
    def update(self, current_index, difference):
        node = self.tree[current_index]
                
        if node.start != node.end:
            self.tree[current_index] = self.merge(self.update(current_index*2+1, difference),
                                                  self.update(current_index*2+2, difference))
            return self.tree[current_index]
        else:
            self.tree[current_index].value += difference
            return self.tree[current_index]
            
if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    
    tree = SegmentTree(data, SegmentNode)

    q = input()
    q = list(map(int, input().split()))
    
    for ii in range(len(q)):
        tree.update(0, q[ii])
        print(tree.tree[0])