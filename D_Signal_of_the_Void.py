import heapq

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    hubs = sorted(zip(b, a))
    
    total_cost = 0
    remaining = n
    heap = []  
    idx = 0
    
    while remaining > 0:
        if heap and heap[0][0] < p:
            cost, cap = heapq.heappop(heap)
            total_cost += cost
            remaining -= 1
            if cap > 1:
                heapq.heappush(heap, (cost, cap - 1))
            
            if idx < n:
                heapq.heappush(heap, (hubs[idx][0], hubs[idx][1]))
                idx += 1
        else:
            total_cost += p
            remaining -= 1
            if idx < n:
                heapq.heappush(heap, (hubs[idx][0], hubs[idx][1]))
                idx += 1
    
    print(total_cost)
