if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())
    encrypted = ""
    
    for ii in range(n):
        if s[ii].isalpha():
            if s[ii].isupper():
                encrypted += chr(ord("A") + (ord(s[ii])-ord("A")+k)%26)
            else:
                encrypted += chr(ord("a") + (ord(s[ii])-ord("a")+k)%26)
        else:
            encrypted += s[ii]
            
    print(encrypted)