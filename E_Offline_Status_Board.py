tests=int(input())
for test in range(tests):
    n=int(input())
    l9=list(map(int,input().split()))
    l12=list(map(int,input().split()))
    i=len(l9)-1
    j=len(l12)-1
    count=0
    while i>=0 and j>=0:
        if l9[i]!=l12[j]:
            count+=1
        else:
            j-=1
        i-=1
    print(count)