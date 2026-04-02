tests=int(input())
for test in range(tests):
    n=int(input())
    s=list(input())
    i=0
    j=n-1
    shifted=False
    possible= True
    while i<j:
        if s[i]!=s[j]:
            if not shifted:
                shifted=True
            else:
                print("No")
                possible=False
                break
        while s[i]!=s[j]:
            i+=1
            j-=1
        i+=1
        j-=1
    if possible:
        print("Yes")
