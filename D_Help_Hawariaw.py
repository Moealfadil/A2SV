tests = int(input())
for _ in range(tests):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    
    b.sort()
    start = b[0]
    
    constructed = []
    
    for i in range(n):
        row_start = start + i * c
        row = []
        for j in range(n):
            row.append(row_start + j * d)
        constructed.extend(row)
    constructed.sort()
    
    if constructed == b:
        print("YES")
    else:
        print("NO")