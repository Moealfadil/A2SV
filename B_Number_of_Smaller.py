n, m= input().split()
n=int(n)
m=int(m)
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
i=0
j=0
count=0
result=[] 
while j < m:
    if arr1[i] < arr2[j]:
        count+=1
        if i==n-1:
            result.append(count)
            result+= [count]*(m-j-1)
            break
        i+=1
    else:
        result.append(count)
        j+=1
print(*result)