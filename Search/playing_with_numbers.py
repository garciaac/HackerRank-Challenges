import math
import sys

tree = []

def build(data):
    global tree
    tree = [None]*2*int(math.pow(2, math.ceil(math.log(len(data), 2))))
    return build_r(0, len(data)-1, 0)

# going one level too deep on build. It's node 5 that has start == end == 2 not node 2. Look into this

def build_r(start, end, current_index):
    global tree
    if start == end:
        tree[current_index] = data[start]
        return tree[current_index]
    else:
        mid = int((start+end)/2)
        tree[current_index] = abs(build_r(start, mid, current_index*2+1)) + abs(build_r(mid+1, end, current_index*2+2))
        return tree[current_index]

def update(current_index, start, end, difference):
    global tree
    print("Current index is "+str(current_index))
    if tree[current_index] is None:
        print ("About to return None for node "+str(current_index))
        print ("Start is "+str(start))
        print ("end is "+str(end))
        return 0
    
    if start != end:
        mid = int((start+end)/2)
        tree[current_index] = abs(update(current_index*2+1, start, mid, difference)) + abs(update(current_index*2+2, mid+1, end, difference))
        return tree[current_index]
    else:
        tree[current_index] += difference
        return tree[current_index]
            
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    
    build(data)
    print(list(map(str, tree)))

    q = input()
    q = list(map(int, sys.stdin.readline().split()))
    
    for ii in range(len(q)):
        update(0, 0, n, q[ii])
        print(list(map(str, tree)))
        sys.stdout.write(str(tree[0])+"\n")