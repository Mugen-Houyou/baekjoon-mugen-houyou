import sys
import heapq
input = sys.stdin.readline

tcs_count = int(input())
for _ in range(tcs_count):
    dcs_count, cq = map(int,input().split()) # 문서 개수, 타깃의 현재 큐값
    tmp_list = list(map(int,input().split())) # 문서 큐 리스트
    cq_doc_val = tmp_list[cq]
    pq = []

    for i in range(len(tmp_list)):
        heapq.heappush(pq, tmp_list[i])

    prv = sys.maxsize
    for i in range(len(pq)):
        popped = heapq.heappop(pq)
        if cq_doc_val == popped:
            while True:
                next = heapq.heappop(pq)
                if popped != next: 
                    heapq.heappush(next)
                    break
            print(dcs_count-i)
            break