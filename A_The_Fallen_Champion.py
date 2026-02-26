n,t=map(int,input().split())
warrios=int(input())
dead=False
for i in range(warrios):
    n2,t2=map(int,input().split())
    if n>n2:
        continue
    elif n==n2 and t<=t2:
        continue
    else:
        print("The Fallen Champion")
        dead=True
        break
if not dead:
    print("The Champion Saves the Accused")