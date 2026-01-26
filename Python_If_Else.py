n=int(input())
if n%2==1:
    print("Weird")
elif n%2==0 and (2<=n<=5 or n>20):
    print("Not Weird")
else:
    print("Weird")