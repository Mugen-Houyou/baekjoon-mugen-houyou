from collections import deque

def rotate_demo():
    # 초기 deque 생성
    dq = deque([1, 2, 3, 4, 5])
    print("원본 deque:", dq)

    # 오른쪽으로 한 칸 회전: 마지막 원소가 첫 위치로 이동
    dq.rotate(1)
    print("rotate(1) 후 (오른쪽으로 한 칸 회전):", dq)

    # deque를 다시 초기 상태로 복원
    dq = deque([1, 2, 3, 4, 5])
    
    # 왼쪽으로 한 칸 회전: 첫 원소가 마지막 위치로 이동
    dq.rotate(-1)
    print("rotate(-1) 후 (왼쪽으로 한 칸 회전):", dq)

    # 추가 예제: 오른쪽으로 두 칸 회전
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(2)
    print("rotate(2) 후 (오른쪽으로 두 칸 회전):", dq)

    # 추가 예제: 왼쪽으로 세 칸 회전
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(-3)
    print("rotate(-3) 후 (왼쪽으로 세 칸 회전):", dq)

if __name__ == "__main__":
    rotate_demo()
