days=int(input())
dic={}
possible=False
for day in range(days):
    n=int(input())
    for i in range(n):
        name, time=input().split()
        time=int(time)
        pair=(name, time)
        if pair in dic:
            dic[pair]+=1
        else:
            dic[pair]=1
for pair in dic:
    if dic[pair]/days>=0.8:
        possible=True
        print("YES")
        break
if not possible:
    print("NO")


    