tests=int(input())
for test in range(tests):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))
    a.sort()
    k.sort(reverse=True)
    n-=1
    m-=1
    count=0
    while n>=0 and m>=0:
        if k[m] > len(a[:n+1]):
            break
        for i in range(k[m]):
            count+=a[n]
            n-=1
        count-=a[n+1]
        m-=1
    count+=sum(a[:n+1])
    print(count)