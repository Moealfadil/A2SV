n, k= map(int, input().split())
if n%2==0:
    half= n//2
else:
    half= n//2+1
if k<= half:
    print(2*k-1)
else:
    print(2*(k-half))
