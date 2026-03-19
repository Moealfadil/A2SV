n,m=[4, 5]
n=int(n)
m=int(m)
books=[3, 1, 2, 1]
i=0
j=0
count=0
mins=0
max_books=0
while j<n:
    if books[j]+mins<=m:
        mins+=books[j]
        count+=1
        max_books=max(max_books,count)
    else:
        while count>0 and books[j]+mins>m:
            mins-=books[i]
            count-=1
            i+=1
    j+=1
print(max_books)
