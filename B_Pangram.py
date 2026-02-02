length=int(input())
words=input().lower()
unique_letters=set()
if length< 26:
    print("NO")
else:
    for letter in words:
        unique_letters.add(letter)
    if len(unique_letters)==26:
        print("YES")
    else:
        print("NO")