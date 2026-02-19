for row in range(5):
    nums=list(map(int,input().split()))
    for col in range(5): 
        if nums[col]==1:
            print(abs(2-row)+abs(2-col))
                