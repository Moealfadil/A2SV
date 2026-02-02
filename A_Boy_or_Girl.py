name=input()
name2=[]
for letter in name:
    if letter not in name2:
        name2.append(letter)
if len(name2)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")