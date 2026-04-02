tests=int(input())
for _ in range(tests):
    n=int(input())
    dic={}
    groups=list(map(int,input().split()))
    skills=list(map(int,input().split()))
    result=[]
    # Create a list for each group
    for i in range(n):
        if groups[i] in dic:
            dic[groups[i]].append(skills[i])
        else:
            dic[groups[i]]=[]
            dic[groups[i]].append(skills[i])
    result = [0] * (n + 1)
    #create a prefix-sum for each group after sorting
    for v in dic.values():
        v.sort(reverse=True)
        
        for i in range(1, len(v)):
            v[i] += v[i-1]
        #choose the sum of skills depending on the number of groups
        m = len(v)
        for k in range(1, m + 1):
            full = m - (m % k) #skills at the end of the list that will not be included in a group will not be counted in sum
            if full > 0:
                result[k] += v[full - 1]
    
    print(*result[1:])
