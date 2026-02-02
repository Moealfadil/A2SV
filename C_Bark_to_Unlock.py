password=input()
num=int(input())
words=[]
string=""
for i in range(num):
    words.append(input())
for word in words:
    for word_2 in words:
        string+=word
        string+=word_2
if password in string:
    print("YES")
else:
    print("NO")

    