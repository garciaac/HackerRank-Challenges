if __name__ == "__main__":
    n = int(input())
    k = int(input())-1
    numbers = list()
    for ii in range(n):
        numbers.append(int(input()))
    numbers = sorted(numbers)
    subset, distance = list(), numbers[len(numbers)-1]-numbers[0]
    for jj in range(len(numbers)-k):
        current_distance = numbers[jj+k]-numbers[jj]
        if current_distance < distance:
            distance = current_distance
            subset = numbers[jj:jj+k+1]
    print(subset[k]-subset[0])