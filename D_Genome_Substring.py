# At a distinguished high school located in Addis Ababa, Ethiopia, a biology lesson was taking place. The topic of the lesson was the genomes. Let's call the genome the string "ACTG".

# Kidus was very bored to sit in his class, so the teacher came up with a task for him: on a given string s
#  consisting of uppercase letters and length of at least 4
# , you need to find the minimum number of operations that you need to apply, so that the genome appears in it as a substring. For one operation, you can replace any letter in the string s
#  with the next or previous in the alphabet. For example, for the letter "D" the previous one will be "C", and the next — "E". In this problem, we assume that for the letter "A", the previous one will be the letter "Z", and the next one will be "B", and for the letter "Z", the previous one is the letter "Y", and the next one is the letter "A".

# Help Kidus solve the problem that the teacher gave him.

# A string a
#  is a substring of a string b
#  if a
#  can be obtained from b
#  by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

# Input
# The first line contains a single integer n
#  (4≤n≤50
# ) — the length of the string s
# .

# The second line contains the string s
# , consisting of exactly n
#  uppercase letters of the Latin alphabet.

# Output
# Output the minimum number of operations that need to be applied to the string s
#  so that the genome appears as a substring in it.

# Examples
# InputCopy
# 4
# ZCTH
# OutputCopy
# 2
# InputCopy
# 5
# ZDATG
# OutputCopy
# 5
# InputCopy
# 6
# AFBAKC
# OutputCopy
# 16
n= int(input())
s= input()  
genome= "ACTG"
min_operations= float('inf')
for i in range(n-3):
    operations= 0
    for j in range(4):
        diff= abs(ord(s[i+j]) - ord(genome[j]))
        operations+= min(diff, 26-diff)
    min_operations= min(min_operations, operations)
print(min_operations)
