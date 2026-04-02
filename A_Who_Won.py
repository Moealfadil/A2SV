tests=int(input())
for i in range(tests):
    first_score=list(map(int,input().split()))
    second_score=list(map(int,input().split()))
    if (second_score[0]>= first_score[1] and first_score[1]> first_score[0] and second_score[0]>= second_score[1]) or (second_score[1]>= first_score[0] and first_score[0]> first_score[1] and second_score[0]<= second_score[1]):
        print("NO")
    else:
        print("YES")