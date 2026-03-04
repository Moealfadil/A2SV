n=int(input())
arr=list(map(int,input().split()))
count=[0]*100
for i in arr:
    count[i]+=1
print(*count)