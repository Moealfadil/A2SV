n, k = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 1

while i < n and arr[i] > k:
    i += 1
    j += 1

if i == n:
    print(0)
    exit()

sum_arr = arr[i]
count = 1
max_count = 1

while j < n:
    while count > 0 and sum_arr + arr[j] > k:
        sum_arr -= arr[i]
        count -= 1
        i += 1

    sum_arr += arr[j]
    count += 1
    max_count = max(max_count, count)
    j += 1

print(max_count)