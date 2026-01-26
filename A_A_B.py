tests= int(input())
for test in range(tests):
    expression= input()
    a,b= expression.split('+')
    result= int(a)+ int(b)
    print(result)