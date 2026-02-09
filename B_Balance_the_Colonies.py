tests= int(input())
for test in range(tests):
    n= int(input())
    if n==2 or n==3:
        print(n)
    else:
        print(n%2)