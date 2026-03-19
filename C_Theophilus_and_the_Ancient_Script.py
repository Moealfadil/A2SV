tests=int(input())
for test in range(tests):
    n=int(input())
    s=input()
    s=list(s)
    count=0
    operation=0
    for i in range(n-1):
        if s[i]=="A" and s[i+1]=="B":
            operation+=count+1
            count=0
            s[i], s[i+1]= s[i+1], s[i]
        elif s[i]=="A":
            count+=1
    print(operation)
