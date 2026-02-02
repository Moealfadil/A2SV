from collections import deque
tests=int(input())
for _ in range(tests):
    n,k=map(int,input().split())
    Hp=list(map(int,input().split()))
    loc=list(map(int,input().split()))
    left=[]
    right=[]
    left_hp=[]
    right_hp=[]
    for i in range(len(loc)):
        if loc[i]<0:
            left.append(loc[i])
            left_hp.append(Hp[i])
        else:
            right.extend(loc[i:])
            right_hp.extend(Hp[i:])
            break
    left=deque(sorted(left))
    right=deque(sorted(right))
    left_hp=deque(left_hp)
    right_hp=deque(right_hp)
    while left or right:
        if left[-1]==0 or right[0]==0:
            print("NO")
            break
        elif not left:
            for bullets in range(k):
                right_hp[0]-=1
                if right_hp[0]<=0:
                    right.popleft()
                    right_hp.popleft()
            right=deque([x - 1 for x in right])
        elif not right:
            for bullets in range(k):
                left_hp[-1]-=1
                if left_hp[-1]<=0:
                    left.pop()
                    left_hp.pop()
            left=deque([x + 1 for x in left])
        else:
            for bullets in range(k):
                if abs(left[-1])<=abs(right[0]):
                    left_hp[-1]-=1
                    if left_hp[-1]<=0:
                        left.pop()
                        left_hp.pop()
                else:
                    right_hp[0]-=1
                    if right_hp[0]<=0:
                        right.popleft()
                        right_hp.popleft()
            left=deque([x + 1 for x in left])
            right=deque([x - 1 for x in right])
    if len(left)==0 and len(right)==0:
        print("YES")
            