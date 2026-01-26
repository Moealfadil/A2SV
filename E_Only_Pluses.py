tests=int(input())
for test in range(tests):
    nums=input()
    a,b,c= map(int, nums.split())
    for i in range(5):
        if a<= b and a<= c:
            a+=1
        elif b<= a and b<= c:
            b+=1
        else:
            c+=1
    print(a*b*c)
