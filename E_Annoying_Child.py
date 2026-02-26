
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    odds = sorted([x for x in a if x % 2 == 1], reverse=True)
    evens = sorted([x for x in a if x % 2 == 0], reverse=True)
    
    o, e = len(odds), len(evens)
    
    prefix_even = [0]
    for x in evens:
        prefix_even.append(prefix_even[-1] + x)
    
    result = []
    for k in range(1, n + 1):
        if o == 0:
            result.append(0)
            continue
        
        max_e = min(e, k - 1)
        min_e = max(0, k - o)
        
        ans = 0
        for num_e in [max_e, max_e - 1]:
            if num_e < min_e or num_e < 0:
                continue
            num_o = k - num_e
            if num_o % 2 == 1 and num_o <= o:
                ans = odds[0] + prefix_even[num_e]
                break
        result.append(ans)
    
    print(' '.join(map(str, result)))