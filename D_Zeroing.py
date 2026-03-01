n, m= input().split()
n=int(n)
m=int(m)
arr=list(map(int,input().split()))
arr.sort()
for i in range(int(m)):
    while len(arr)>0 and arr[0]==0:
        arr.pop(0)
    if len(arr)==0:
        print(0)
    else:
        minimum=arr[0]
        print(minimum)
        arr=[x-minimum for x in arr] 
        


        

