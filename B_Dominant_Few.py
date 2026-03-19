tests = int(input())
for test in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    elite = 0
    crowd=0
    crowdpower=a[0]
    elitepower=0
    possible = False
    i=n-1
    j=1
    check=1
    while j < i:
        elite+=1
        crowd+=1
        crowdpower += a[j]
        elitepower += a[i]
        i-=1
        j+=1
        if elitepower > crowdpower:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")
    
