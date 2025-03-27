import sys
input = sys.stdin.readline

def largest_cross_area(histo_arr, start, mid, end):
    # 이 함수는 중간 영역의 가능한 최대 넓이를 계산함

    # left와 right는 중간 경계를 넘어서 확장될 인덱스들
    left = mid
    right = mid + 1

    # 초기 구간의 높이는 두 막대 중 작은 값이며, 넓이는 2*height
    height = min(histo_arr[left], histo_arr[right])
    max_area = height * 2

    # while에서 확장 => 좌측 또는 우측으로 확장하기
    while left > start or right < end:
        if right < end and (left == start or histo_arr[left - 1] < histo_arr[right + 1]):
            # 만약 오른쪽으로 확장이 가능한 상태이면서, 
            # 왼쪽 확장은 불가능하거나( left == start ),
            # 오른쪽의 다음 막대가 왼쪽의 다음 막대보다 크다면,
            # 오른쪽으로 확장
            right += 1
            height = min(height, histo_arr[right])
        else:
            # 이외에는 왼쪽으로 확장
            left -= 1
            height = min(height, histo_arr[left])
        # 현재 구간의 넓이 계산 후 최댓값 갱신
        max_area = max(max_area, height * (right - left + 1))
    return max_area


def largest_rectangle(histo_arr, start, end):
    # 이 함수는 분할 정복 부분

    # 기저 사례: 구간에 막대가 한 개만 있다면 그 높이가 넓이가 된다.
    if start == end:
        return histo_arr[start]

    # 중간 인덱스 계산
    mid = (start + end) // 2

    # 왼쪽 구간, 오른쪽 구간에 대해 재귀적으로 최대 넓이 구하기
    left_area = largest_rectangle(histo_arr, start, mid)
    right_area = largest_rectangle(histo_arr, mid + 1, end)

    # 중앙을 가로지르는 최대 넓이 구하기
    cross_area = largest_cross_area(histo_arr, start, mid, end)

    # 세 구간 중 최댓값 반환
    return max(left_area, right_area, cross_area)


while True:
    # 한 줄씩 읽으며 테스트 케이스 처리: 첫 숫자는 막대의 개수
    data = list(map(int, input().split()))

    if not data: continue
    if data[0] == 0: break

    n = data[0]
    histo_arr = data[1:]
    print(largest_rectangle(histo_arr, 0, n - 1))