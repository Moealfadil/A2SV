tests=int(input())
for test in range(tests):
    n, m=input().split()
    n=int(n)
    m=int(m)
    arr=list(map(int,input().split()))
    arr.sort()
    result=[]
    for i in range(m):
        opperation, lower, upper=input().split()
        lower=int(lower)
        upper=int(upper)
        if lower> max(arr) or upper<min(arr):
            result.append(max(arr))
        else:
            if opperation=="+":
                for j in range(n):
                    if arr[j]>upper:
                        break
                    else:
                        if arr[j]>=lower and arr[j]<=upper:
                            arr[j]+=1
            else:
                for j in range(n):
                    if arr[j]>upper:
                        break
                    else:
                        if arr[j]>=lower and arr[j]<=upper:
                            arr[j]-=1
            result.append(arr[-1])
    print(" ".join(map(str,result)))