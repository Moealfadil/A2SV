n, m =input().split()
n=int(n)-1
m=int(m)-1
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=[]
i=0
j=0
for _ in range(n+m+2):
    if i<=n and arr1[i]<=arr2[j]:
        c.append(arr1[i])
        if i==n:
            c+=arr2[j:]
            break
        i+=1
    elif j<=m and arr1[i]>arr2[j]:
        c.append(arr2[j])
        if j==m:
            c+=arr1[i:]
            break
        j+=1
print(c)