# In the ancient days of the Seven Kingdoms, when alliances were forged in grand councils and every noble house sought to prove its worth before the Iron Throne, the order in which decisions were made could determine victory or defeat.

# During the Great Council at King’s Landing, Lord Simanga of House Baratheon has gathered n
#  noble houses to participate in a royal card trial.

# The Iron Throne possesses a deck of n⋅m
#  enchanted cards numbered from 0
#  to n⋅m−1
# . The cards are distributed so that each of the n
#  houses receives exactly m
#  cards.

# To ensure fairness among the Seven Kingdoms, only one house may play one card per round. Thus, Lord Simanga must determine a turn order, defined by a permutation∗
#  p
#  of length n
# , such that the pi
# -th house plays the i
# -th card in each round.

# In other words, during each round, the following events occur in order:

# The p1
# -th house places any card from its deck on top of the central pile.
# The p2
# -th house places any card from its deck on top of the central pile.
# …
# The pn
# -th house places any card from its deck on top of the central pile.
# However, there is a decree of the Iron Throne. Initially, the central pile contains a card numbered −1
# . In order to place a card, its number must be strictly greater than the number currently on top of the central pile. Once placed, that card becomes the new top card.

# If a house is unable to place any valid card during its turn, the trial is declared lost.

# Lord Yerosen, Hand of the King, wonders: does there exist a permutation p
#  such that all houses can empty their decks after exactly m
#  rounds? If such a permutation exists, output any valid p
# . Otherwise, output −1
# .

# ∗
# A permutation of length n
#  contains each integer from 1
#  to n
#  exactly once

# Input
# The first line contains an integer t
#  (1≤t≤400
# ) — the number of test cases.

# The first line of each test case contains two integers n
#  and m
#  (1≤n⋅m≤2000
# ) — the number of houses and the number of cards each house receives.

# The following n
#  lines contain m
#  integers each — the cards received by each house. It is guaranteed that all given numbers (across all n
#  lines) are distinct and lie in the range from 0
#  to n⋅m−1
# , inclusive.

# It is guaranteed that the sum of n⋅m
#  over all test cases does not exceed 2000
# .

# Output
# For each test case, output the following on a new line:

# If a valid permutation p
#  exists, output n
#  space-separated integers p1,p2,…,pn
# .
# Otherwise, output −1
# .
# Example
# InputCopy
# 4
# 2 3
# 0 4 2
# 1 5 3
# 1 1
# 0
# 2 2
# 1 2
# 0 3
# 4 1
# 1
# 2
# 0
# 3
# OutputCopy
# 1 2
# 1
# -1
# 3 1 2 4
# Note
# In the first test case, one valid turn order is to let the first house act before the second house. The cards played will be 0→1→2→3→4→5
# .

# In the second test case, there is only one house, so playing its cards in increasing order will empty its deck.

# In the third test case, it can be shown that no valid turn order allows all cards to be played.
tests = int(input())
for _ in range(tests):
    n, m = map(int, input().split())
    arrays = []
    for i in range(n):
        arr = list(map(int, input().split()))
        arr.sort()
        arrays.append((arr, i + 1))
    
    order = sorted(arrays, key=lambda x: x[0])
    
    possible = True
    for col in range(m):
        for j in range(n - 1):
            if order[j][0][col] >= order[j + 1][0][col]:
                possible = False
                break
        if not possible:
            break
    if possible:
        for col in range(m - 1):
            if order[n - 1][0][col] >= order[0][0][col + 1]:
                possible = False
                break
    
    if possible:
        print(" ".join(str(order[i][1]) for i in range(n)))
    else:
        print(-1)
