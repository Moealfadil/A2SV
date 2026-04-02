tests = int(input())
for _ in range(tests):
    s = input()
    
    good = set()
    i = 0
    
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        if (j - i) % 2 == 1:
            good.add(s[i])
        
        i = j
    
    print("".join(sorted(good)))


