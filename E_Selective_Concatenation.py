# In the A2SV remote classroom, students are divided into exactly k study groups. However, only the even-numbered groups submit their work for evaluation. The submissions are merged in order, and the instructor checks how well they match the expected sequence starting from 1.

# You are given an array a
#  of length n
#  and an even integer k
#  (2≤k≤n
# ). You need to split the array a
#  into exactly k
#  non-empty subarrays†
#  such that each element of the array a
#  belongs to exactly one subarray.

# Next, all subarrays with even indices (second, fourth, …
# , k
# -th) are concatenated into a single array b
# . After that, 0
#  is added to the end of the array b
# .

# The cost of the array b
#  is defined as the minimum index i
#  such that bi≠i
# . For example, the cost of the array b=[1,2,4,5,0]
#  is 3
# , since b1=1
# , b2=2
# , and b3≠3
# . Determine the minimum cost of the array b
#  that can be obtained with an optimal partitioning of the array a
#  into subarrays.

# †
# An array x
#  is a subarray of an array y
#  if x
#  can be obtained from y
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (2≤k≤n≤2⋅105
# , k
#  is even) — the length of the array a
#  and the number of subarrays.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array a
# .

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the minimum cost of the array b
#  that can be obtained.

# Example
# InputCopy
# 4
# 3 2
# 1 1 1
# 8 8
# 1 1 2 2 3 3 4 4
# 5 4
# 1 1 1 2 2
# 5 4
# 1 1 1000000000 2 2
# OutputCopy
# 2
# 5
# 2
# 1
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    from collections import Counter
    cnt = Counter(a)
    
    half = k // 2
    cost = 1
    taken = 0
    
    while taken < half:
        if cnt[cost] > 0:
            cnt[cost] -= 1
            taken += 1
        else:
            break
        if taken < half and cnt[cost] == 0:
            cost += 1
    
    if taken == half:
        cost += 1
    
    print(cost)

