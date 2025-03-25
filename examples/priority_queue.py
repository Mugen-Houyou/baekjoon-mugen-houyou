import heapq

def heapq_priority_queue_demo():
    # 빈 리스트를 우선순위 큐(최소 힙)로 사용
    pq = []
    
    # (우선순위, 데이터) 튜플을 삽입
    # 숫자가 작을수록 높은 우선순위
    heapq.heappush(pq, (2, '작업 B'))
    heapq.heappush(pq, (1, '작업 A'))
    heapq.heappush(pq, (3, '작업 C'))
    
    print("우선순위 큐 상태:", pq)
    
    # 우선순위가 높은 항목부터 하나씩 꺼내기
    while pq:
        priority, task = heapq.heappop(pq)
        print("처리된 작업:", task, "우선순위:", priority)

def heapq_priority_queue_advanced_demo():
    # 1. heapify: 리스트를 힙으로 변환
    data = [5, 7, 9, 1, 3]
    heapq.heapify(data)
    print("heapify 후:", data)   # 힙 구조로 변환된 리스트

    # 2. heappushpop: 새로운 원소를 넣고, 최소 원소를 꺼냄
    result = heapq.heappushpop(data, 4)
    print("heappushpop 결과:", result)
    print("heappushpop 후 heap:", data)

    # 3. heapreplace: 최소 원소를 제거하고 새로운 원소 삽입
    result = heapq.heapreplace(data, 6)
    print("heapreplace 결과:", result)
    print("heapreplace 후 heap:", data)

    # 4. nlargest와 nsmallest: 이터러블에서 가장 큰/작은 n개의 원소 반환
    largest = heapq.nlargest(3, data)
    smallest = heapq.nsmallest(3, data)
    print("3개의 가장 큰 원소:", largest)
    print("3개의 가장 작은 원소:", smallest)

heapq_priority_queue_demo()