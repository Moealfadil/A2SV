from collections import Counter

n = int(input())
s = input().strip()

counts = Counter(s)

if len(counts) == 1:

   print("Yes")

elif all(v == 1 for v in counts.values()):
   
   print("No")

else:
   
   print("Yes")
