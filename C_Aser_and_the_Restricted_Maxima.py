import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    if k == 1:
        if '1' in s:
            print("NO")
        else:
            print("YES")
            print(*range(1, n + 1))
        return

    run = 0
    for c in s:
        run = run + 1 if c == '1' else 0
        if run >= k:
            print("NO")
            return

    zeros = [i for i, c in enumerate(s) if c == '0']
    z = len(zeros)

    def rightmost_zero_in(lo, hi):
        l, r, res = 0, z - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if zeros[mid] <= hi:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        if res == -1 or zeros[res] < lo:
            return -1
        return zeros[res]

    anchors = []
    anchor_set = set()
    cur = -1

    # Need every window of size k covered, so last anchor must be >= n-k
    while True:
        lo = cur + 1
        hi = cur + k - 1
        if hi >= n:
            hi = n - 1

        anchor = rightmost_zero_in(lo, hi)
        if anchor == -1:
            print("NO")
            return

        anchors.append(anchor)
        anchor_set.add(anchor)
        cur = anchor

        # Stop once the anchor covers the last window
        if cur >= n - k:
            break

    p = [0] * n
    m = len(anchors)
    for i, pos in enumerate(anchors):
        p[pos] = n - i

    val = 1
    for i in range(n):
        if i not in anchor_set:
            p[i] = val
            val += 1

    print("YES")
    print(*p)

t = int(input())
for _ in range(t):
    solve()