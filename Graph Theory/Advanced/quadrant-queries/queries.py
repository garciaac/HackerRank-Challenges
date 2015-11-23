import math

class SegmentNode:
    pass

class GraphQueryNode(SegmentNode):
    def __init__(self, value, start, end):
        self.value = value
        self.start = start
        self.end = end
        self.null_value = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0
        }
    
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
            
        merge = dict(self.value)
        for key in merge:
            merge[key] += other.value[key]
        return GraphQueryNode(merge, start, end)
    
    def __radd__(self, other):
        return self + other
    
    def __str__(self):
        return " ".join([str(self.value["1"]), str(self.value["2"]), str(self.value["3"]), str(self.value["4"])])

class SegmentTree:
    def __init__(self, data, node_type):
        self.tree = [None]*2*int(math.pow(2, math.ceil(math.log(len(data), 2))))
        self.data = data
        self.node_type = node_type
        self.build(0, len(data)-1, 0)
    
    def __str__(self):
        string = ""
        for ii in range(len(self.tree)):
            string += "Index "+str(ii)+": "+str(self.tree[ii])+"\n"
        return string
    
    def build(self, start, end, current_index):
        if start == end:
            self.tree[current_index] = self.node_type(self.data[start], start, end)
            return self.tree[current_index]
        else:
            midpoint = int((start+end)/2)
            self.tree[current_index] = self.merge(self.build(start, midpoint, current_index*2+1),
                                                  self.build(midpoint+1, end, current_index*2+2))
            return self.tree[current_index]        

    def query(self, current_index, start, end):
        node = self.tree[current_index]
        if start <= node.start and end >= node.end:
            return node
        elif node.end < start or node.start > end:
            return None
        else:
            return self.merge(self.query(current_index*2+1, start, end),
                              self.query(current_index*2+2, start, end))
    
    def merge(self, left_node, right_node):
        return left_node + right_node
    
    def update(self, current_index, start, end, functor, args):
        node = self.tree[current_index]
        if start <= node.start and end >= node.end and node.start == node.end:
            self.tree[current_index] = functor(node, args)
            return self.tree[current_index]
            
        elif end < node.start or start > node.end:
            return self.tree[current_index]
        else:
            self.tree[current_index] = self.merge(self.update(current_index*2+1, start, end, functor, args),
                                                  self.update(current_index*2+2, start, end, functor, args))
            return self.tree[current_index]

        
def reflect(node, update_type):
    temp = dict(node.value)
    if update_type == "X":
        node.value["1"] = temp["4"]
        node.value["2"] = temp["3"]
        node.value["3"] = temp["2"]
        node.value["4"] = temp["1"]
    elif update_type == "Y":
        node.value["1"] = temp["2"]
        node.value["2"] = temp["1"]
        node.value["3"] = temp["4"]
        node.value["4"] = temp["3"]
    return node
            
if __name__ == "__main__":
    with open("case7-input.txt") as infile:
#        n = int(input())
        n = int(infile.readline())
        x, y, data = [], [], []
        for ii in range(n):
            temp = list(map(int, infile.readline().split()))
            x.append(temp[0])
            y.append(temp[1])
            if x[ii] > 0 and y[ii] > 0:
                data.append({"1": 1, "2": 0, "3": 0, "4": 0})
            elif x[ii] < 0 and y[ii] > 0:
                data.append({"1": 0, "2": 1, "3": 0, "4": 0})
            elif x[ii] < 0 and y[ii] < 0:
                data.append({"1": 0, "2": 0, "3": 1, "4": 0})
            else:
                data.append({"1": 0, "2": 0, "3": 0, "4": 1})

        tree = SegmentTree(data, GraphQueryNode)
        
        # Need to combine update functions. Could keep an array of the same size as the
        # input data set. Initialize it with 1s, and then every time a reflection happens,
        # multiply the interval by -1. Then, after a series of updates before a count query,
        # any index with -1 needs to be reflected. It might work.
        
        q = int(infile.readline())
        for ii in range(q):
            query_type, start, end = infile.readline().split()
            start, end = int(start), int(end)
            if query_type == "C":
                print(str(tree.query(0, start-1, end-1)))
            else:
                tree.update(0, start-1, end-1, reflect, query_type)
        
    
    