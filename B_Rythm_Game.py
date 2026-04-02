tests=int(input())
for _ in range(tests):
    n ,k= map(int,input().split())
    s=input()
    idx=-k
    count=0
    for i in range(n):
        if s[i]=="1":
            if idx<i-(k-1):
                count+=1
            idx=i
    print(count)
