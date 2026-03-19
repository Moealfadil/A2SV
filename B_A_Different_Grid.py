tests= int(input())
for test in range(tests):
    m, n= map(int, input().split())
    grid= []
    if m==1 and n==1:
        element= int(input())
        print(-1)
        continue
    elif m==1:
        row= list(map(int, input().split()))
        row.sort(reverse=True)
        print(*row)
    else:
        for i in range(m):
            row= list(map(int, input().split()))
            row.reverse()
            grid.append(row)
        grid.reverse()
        for i in range(m):
            print(*grid[i])