tests=int(input())
for test in range(tests):
    machine={}
    result=0
    n, k=map(int, input().split())
    for i in range(k):
        a, b=map(int, input().split())
        if a in machine:
            machine[a]+=b
        else:
            machine[a]=b
    max_box= sorted(machine.items(), key=lambda x: x[1], reverse=True)
    for j in range(len(max_box)):
        if j==n:
            break
        else:
            result+=max_box[j][1]
    print(result)

        