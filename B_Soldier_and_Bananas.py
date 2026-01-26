k, n, w= map(int, input().split())
total=sum(list(range(1, w+1))) * k
print(total-n if total> n else 0)