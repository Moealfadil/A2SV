import collections
n = int(input())
numbers = list(map(int, input().split()))
d = collections.deque(numbers)
sereja_score = 0
dima_score = 0
for i in range(n):
    if i % 2 == 0:
        if d[0] >= d[-1]:
            sereja_score += d.popleft()
        else:
            sereja_score += d.pop()
    else:
        if d[0] >= d[-1]:
            dima_score += d.popleft()
        else:
            dima_score += d.pop()
print(sereja_score, dima_score)