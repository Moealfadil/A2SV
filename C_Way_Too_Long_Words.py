tests=int(input())
for test in range(tests):
    word= input()
    if len(word)>10:
        abbreviated= word[0]+ str(len(word)-2)+ word[-1]
        print(abbreviated)
    else:
        print(word)