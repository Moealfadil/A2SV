tests=int(input())
for test in range(tests):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    i=0
    j=0
    count=0
    while j<n:
        if a[i]>b[j]:
            count+=1
        else:
            i+=1
        j+=1
    print(count)
