tests=int(input())
for test in range(tests):
    n, m=input().split()
    n=int(n)
    m=int(m)
    arr=list(map(int,input().split()))
    maxx=max(arr)
    result=[]
    for i in range(m):
        opperation, lower, upper=input().split()
        lower=int(lower)
        upper=int(upper)
        if opperation=="+" and lower<=maxx<=upper:
            maxx+=1
        elif opperation=="-" and lower<=maxx<=upper:
            maxx-=1
        result.append(maxx)
    print(" ".join(map(str,result)))