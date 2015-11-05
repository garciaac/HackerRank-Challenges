if __name__ == "__main__":
    for case in range(int(input())):
        n = int(input())
        if n%3 == 0:
            print("5"*n)
        else:
            num_threes = 0
            num_remaining_digits = n
            answer = -1
            while ((num_remaining_digits % 3) != 0) and num_remaining_digits > 0:
                num_threes += 5
                num_remaining_digits -= 5
            if (num_remaining_digits < 0):
                print(answer)
            else:
                print ("5"*num_remaining_digits+"3"*num_threes)