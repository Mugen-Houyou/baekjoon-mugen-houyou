def merge(left_arr, right_arr):
    merged_result = []  # 병합된 결과를 저장할 리스트
    i = j = 0

    # 두 배열을 비교하며 작은 값을 순서대로 병합
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged_result.append(left_arr[i])
            i += 1
        else:
            merged_result.append(right_arr[j])
            j += 1

    # 남은 요소들을 그대로 추가
    merged_result.extend(left_arr[i:])
    merged_result.extend(right_arr[j:])
    return merged_result

def merge_sort(arr):
    # 배열의 길이가 1 이하? 이미 정렬 완료임. 즉, 그대로 반환
    if len(arr) <= 1: return arr

    # 배열을 반으로 나눔
    mid_idx = len(arr) // 2
    left_arr = merge_sort(arr[:mid_idx])
    right_arr = merge_sort(arr[mid_idx:])

    # 두 배열의 정렬 및 반환
    return merge(left_arr, right_arr)


sample = [38, 27, 43, 3, 9, 82, 10, 12, 34, 45, 13, 26, 1, 64, 43, 93, 50, 4, 2, 8]
print("원본 배열:", sample)
sorted_arr = merge_sort(sample)
print("정렬 후 배열:", sorted_arr)
