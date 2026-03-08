tests = int(input())
for test in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    elite = []
    coward=[a[0]]
    possible = False
    i=n-1
    j=1
    check=1
    while check < n:
        elite.append(a[i])
        coward.append(a[j])
        i-=1
        j+=1
        if n%2==0:
            check = len(elite)+len(coward)+1
        else:
            check = len(elite)+len(coward)
        if sum(elite) > sum(coward):
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")
    
